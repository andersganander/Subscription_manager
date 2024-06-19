import datetime
import json
from collections import OrderedDict
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.db.models import Count, Sum, Prefetch
from django.db import IntegrityError

from services.models import Service
from .forms import SubscriptionForm, SubscriptionEditForm
from .models import Subscription, User 

#from django.http import HttpResponse

def subscriptions_view(request):
    """
    This function is responsible for displaying a list of subscriptions for the authenticated user.
    It checks if the user is authenticated, filters subscriptions based on the user, and orders them by subscription name.
    It also calculates the total number of subscriptions and the current date.
    The function then calls the 'summarize_subscriptions' function to get the summary of subscriptions.
    Finally, it passes the necessary data to the 'subscription_list.html' template for rendering.

    Parameters:
    request (HttpRequest): The request object containing information about the current HTTP request.

    Returns:
    HttpResponse: The rendered 'subscription_list.html' template with the necessary context data.
    """

    # check for user
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    # Get the subscriptions
    subscriptions = Subscription.objects.filter(subscriber=request.user).order_by('subscription_name')
    today = datetime.date.today()
    # Get the summary of subscriptions
    summary = summarize_subscriptions(subscriptions)
    context = {'subscriptions' : subscriptions, 'summary': summary, 'today': today}
    return render(request, 'subscription_list.html', context)

def subscriptions_summary_view(request):
    """
    Function responsible for displaying a summary of subscriptions.
    It filters the subscriptions based on the current user and only includes active subscriptions.
    It then calls the 'categories_total' and 'summarize_subscriptions' functions to get the necessary data.
    The data is then passed to the 'subscription_summary.html' template for rendering.

    Parameters:
    request (HttpRequest): The request object containing information about the current HTTP request.

    Returns:
    HttpResponse: The rendered 'subscription_summary.html' template with the necessary context data.
    """
    subscriptions = Subscription.objects.filter(subscriber=request.user, active=True)
    cat_summary = categories_total(request, subscriptions)
    summary = summarize_subscriptions(subscriptions)
    context = {'cat_summary': cat_summary, 'summary': summary}
    return render(request, 'subscription_summary.html', context)

def subscription_form_view(request):
    """
    Function that handles the add subscription form. It processes POST requests and saves new subscriptions.
    If the request method is POST, it validates the form data, creates a new subscription object, adds relations,
    and saves it to the database. If the service name already exists, it shows an error message.
    If the request method is not POST, it renders the subscription form with a list of services.

    Parameters:
    request (HttpRequest): The request object containing information about the current HTTP request.

    Returns:
    HttpResponse: The rendered 'add_subscription.html' template with the necessary context data or a redirect to the subscriptions page.
    """
    if request.method == 'POST':
        # Handle POST data from the form
        form = SubscriptionForm(data=request.POST)
        if form.is_valid():
            price = form.cleaned_data['monthly_price']
            # Add relations
            subscription = form.save(commit=False)
            subscription.subscriber = request.user
            subscription.subscription_category = subscription.service.category

            # Save object and show success message
            try:
                subscription.save()
            except IntegrityError as e:
                messages.add_message(
                    request, messages.ERROR, 'The service name already exists, change the name.'
                )
                return redirect('/subscriptions/add')

            form = SubscriptionForm()
            messages.add_message(
                request, messages.SUCCESS,
                'Subscription successfully added'
            )
            return redirect('/subscriptions')
    else:
        form = SubscriptionForm()
        services = Service.objects.all().order_by('name').values('name', 'default_price')
        services_dict = {service['name']: service['default_price'] for service in services}
        services_dict_sorted = OrderedDict(sorted(services_dict.items()))
        context = {'services_dict': services_dict_sorted, 'form': form}
        return render(request, 'add_subscription.html', context)

    return render(request, 'add_subscription.html', {'form': form})

def subscription_edit_view(request, subscription_id):
    """
    This function handles the edit subscription view. It retrieves a subscription object based on the provided subscription_id.
    If the request method is POST, it validates the form data, updates the subscription object, and saves it to the database.
    If the request method is not POST, it renders the subscription edit form with the existing subscription data.

    Parameters:
    request (HttpRequest): The request object containing information about the current HTTP request.
    subscription_id (int): The unique identifier of the subscription to be edited.

    Returns:
    HttpResponse: The rendered 'edit_subscription.html' template with the necessary context data or a redirect to the subscriptions page.
    """

    # Get the subscription
    subscription = get_object_or_404(Subscription, pk=subscription_id)

    if request.method == 'POST':
        # Handle POST data from the form
        form = SubscriptionEditForm(data=request.POST, instance=subscription)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Subscription successfully saved'
            )
            return redirect('/subscriptions')
    else:
        # Checks if there already is a reminder adress for the subscription
        if subscription.reminder_email:
            user_email = subscription.reminder_email
        else:
            # Use user_email
            user_email = User.objects.get(username=subscription.subscriber).email

        if user_email:
            subscription.reminder_email = user_email
        
        form = SubscriptionEditForm(instance=subscription)
        return render(request, 'edit_subscription.html', {'form': form, 'subscription': subscription})

def subscription_delete_view(request, subscription_id):
    """
    Handles the deletion of a subscription. It retrieves a subscription object based on the provided subscription_id.
    If the subscription exists, it is deleted from the database and a success message is displayed.

    Parameters:
    request (HttpRequest): The request object containing information about the current HTTP request.
    subscription_id (int): The unique identifier of the subscription to be deleted.

    Returns:
    HttpResponse: A redirect to the subscriptions page after deleting the subscription.
    """

    subscription = Subscription.objects.filter(id=subscription_id)
    if subscription.exists():
        subscription.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Subscription successfully deleted'
        )
    return redirect('/subscriptions')


def summarize_subscriptions(subscriptions):
    """
    Calculates the total number of active subscriptions and the total monthly price for a given list of subscriptions.

    Parameters:
    subscriptions (QuerySet): A QuerySet of Subscription objects.

    Returns:
    dict: A dictionary containing the total number of active subscriptions ('total_active') and the total monthly price ('total_price').
    """

    total_active = 0
    total_price = 0
    for subscription in subscriptions:
        if subscription.active == True:
            total_active += 1
            total_price += subscription.monthly_price
    
    summary_dict = {
        'total_active': total_active,
        'total_price': total_price
    }

    return summary_dict

def categories_total(request, subscriptions):
    """
    Calculates the total number of subscriptions per category and the total cost for each category.
    It uses Django's QuerySet API to fetch and process the data.

    Parameters:
    request (HttpRequest): The request object containing information about the current HTTP request.
    subscriptions (QuerySet): A QuerySet of Subscription objects.

    Returns:
    list: A list of dictionaries, where each dictionary represents a category.
          Each dictionary contains the category name, subscription count, and total cost.
    """
    subscriptions_categories = subscriptions.prefetch_related(Prefetch('subscription_category'))
  
    # Group by category and aggregate count and total cost
    categories = (
        subscriptions_categories
       .values('subscription_category__name')
       .annotate(subscription_count=Count('id'), total_cost=Sum('monthly_price'))
    )
    
    # Convert queryset to list of dictionaries
    categories_list = [{"category_name": item['subscription_category__name'], "subscription_count": item["subscription_count"], "total_cost": item["total_cost"]} for item in categories]
    
    return categories_list

def about_view(request):
    """
    This function handles the about view. It renders the 'about.html' template.

    Parameters:
    request (HttpRequest): The request object containing information about the current HTTP request.

    Returns:
    HttpResponse: The rendered 'about.html' template.
    """
    
    return render(request, 'about.html')