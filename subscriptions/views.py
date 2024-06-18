import datetime
import json
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.db.models import Count, Sum, Prefetch
from django.db import IntegrityError

from services.models import Service
from .forms import SubscriptionForm, SubscriptionEditForm
from .models import Subscription, User 

#from django.http import HttpResponse

def subscriptions_view(request):
    # check for user
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    ###
    subscriptions = Subscription.objects.filter(subscriber=request.user)
    #subscriptions = Subscription.objects.all()
    print(f"User: {request.user}")
    print(f"Antal pren: {subscriptions.count()}")
    print(f"Today: {datetime.date.today()}")
    today = datetime.date.today()
    summary = summarize_subscriptions(subscriptions)
    #print(categories_total(subscriptions))
    context = {'subscriptions' : subscriptions, 'summary': summary, 'today': today}
    #return HttpResponse("<h1>Subscriptions</h1>")
    return render(request, 'subscription_list.html', context)

def subscriptions_summary_view(request):
    """
    This view function is responsible for displaying a summary of subscriptions.
    It filters the subscriptions based on the current user and only includes active subscriptions.
    It then calls the 'categories_total' and 'summarize_subscriptions' functions to get the necessary data.
    The data is then passed to the 'subscription_summary.html' template for rendering.

    Parameters:
    request (HttpRequest): The request object containing information about the current HTTP request.

    Returns:
    HttpResponse: The rendered 'subscription_summary.html' template with the necessary context data.
    """
    subscriptions = Subscription.objects.filter(subscriber=request.user, active=True)
    print(f"Cat Summary User: {request.user}")
    print(f"Cat Summary Antal pren: {subscriptions.count()}")
    cat_summary = categories_total(request, subscriptions)
    summary = summarize_subscriptions(subscriptions)
    context = {'cat_summary': cat_summary, 'summary': summary}
    return render(request, 'subscription_summary.html', context)

def subscription_form_view(request):
    """
    This view function handles the subscription form. It processes POST requests and saves new subscriptions.
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
            #service_name = form.cleaned_data['service_name']
            price = form.cleaned_data['monthly_price']
            print(f"User: {request.user}")
            #print(f"Form service_name: {service_name}")
            print(f"Form price: {price}")
            # Add relations
            subscription = form.save(commit=False)
            subscription.subscriber = request.user
            subscription.subscription_category = subscription.service.category
            #service = Service.objects.get(name=service_name)
            #subscription.service = service

            # Save object and show success message
            try:
                subscription.save()
            except IntegrityError as e:
                messages.add_message(
                    request, messages.ERROR, 'The service name already exists, choose another one'
                )
                return redirect('/subscriptions/add')
            form = SubscriptionForm()
            messages.add_message(
                request, messages.SUCCESS,
                'Subscription successfully added'
            )
            return redirect('/subscriptions')
        # else:
        #     messages.add_message(
        #         request, messages.ERROR,
        #         'Subscription could not be added'
        #     )
        #     return redirect('/subscriptions/add')
    else:
        form = SubscriptionForm()
        services = Service.objects.all().values('name', 'default_price')  # Fetch data
        services_dict = {service['name']: service['default_price'] for service in services}
        context = {'services_dict': services_dict, 'form': form}
        return render(request, 'add_subscription.html', context)

    return render(request, 'add_subscription.html', {'form': form})

def subscription_edit_view(request, subscription_id):
    subscription = get_object_or_404(Subscription, pk=subscription_id)

    if request.method == 'POST':
        # Handle POST data from the form
        print("POST")
        form = SubscriptionEditForm(data=request.POST, instance=subscription)
        if form.is_valid():
            print("FORM IS VALID")
            form.save()
            print("FORM SAVED")
            messages.add_message(
                request, messages.SUCCESS,
                'Subscription successfully saved'
            )
            return redirect('/subscriptions')
    else:
        print(f"SUBSCRIPTION: {subscription.subscriber}")
        #Customer.objects.filter(id=customer_id).first()
        # get email from user object and set reminder_email

        if subscription.reminder_email:
            user_email = subscription.reminder_email
        else:
            user_email = User.objects.get(username=subscription.subscriber).email

        if user_email:
            print(f"user_email: {user_email}")
            subscription.reminder_email = user_email
            print(f"subscription.reminder_email: {subscription.reminder_email}")
        
        form = SubscriptionEditForm(instance=subscription)
        #print (f"Subscription_edit_view Subscription-id: {subscription_id}")
        return render(request, 'edit_subscription.html', {'form': form, 'subscription': subscription})

def subscription_delete_view(request, subscription_id):
    subscription = Subscription.objects.filter(id=subscription_id)
    if subscription.exists():
        subscription.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Subscription successfully deleted'
        )
    return redirect('/subscriptions')


def summarize_subscriptions(subscriptions):
    #print(f"subscriptions: {subscriptions}")
    #print(f"subscriptions.count(): {subscriptions.count()}")
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

    print(f"summary_dict: {summary_dict}")
    return summary_dict

def categories_total(request, subscriptions):
    #active_subscriptions = Subscription.objects.filter(active=True)
    #subscriptions_categories = Subscription.objects.filter(subscriber=request.user, active=True)
    #subscriptions_categories = Subscription.objects.prefetch_related(Prefetch('subscription_category'))
    subscriptions_categories = subscriptions.prefetch_related(Prefetch('subscription_category'))

    print(f"subscriptions_categories: {subscriptions_categories}")
  
  
    # Group by category and aggregate count and total cost
    categories = (
        subscriptions_categories
       .values('subscription_category__name')
       .annotate(subscription_count=Count('id'), total_cost=Sum('monthly_price'))
    )
    
    # Convert queryset to list of dictionaries
    categories_list = [{"category_name": item['subscription_category__name'], "subscription_count": item["subscription_count"], "total_cost": item["total_cost"]} for item in categories]
    
    #return JsonResponse(categories_list, safe=False)
    return categories_list

def about_view(request):
    return render(request, 'about.html')