import datetime
import json
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.db.models import Count, Sum, Prefetch

from services.models import Service
from .forms import SubscriptionForm, SubscriptionEditForm
from .models import Subscription 

#from django.http import HttpResponse

def subscriptions_view(request):
    # check for user
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
    subscriptions = Subscription.objects.filter(subscriber=request.user, active=True)
    print(f"Cat Summary User: {request.user}")
    print(f"Cat Summary Antal pren: {subscriptions.count()}")
    cat_summary = categories_total(request, subscriptions)
    summary = summarize_subscriptions(subscriptions)
    context = {'cat_summary': cat_summary, 'summary': summary}
    return render(request, 'subscription_summary.html', context)

def subscription_form_view(request):
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
            #service = Service.objects.get(name=service_name)
            #subscription.service = service

            # Save object and show success message
            subscription.save()  
            form = SubscriptionForm()
            messages.add_message(
                request, messages.SUCCESS,
                'Subscription added'
            )
            return redirect('/subscriptions')
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
                'Subscription edited'
            )
            return redirect('/subscriptions')
    else:
        print(f"SUBSCRIPTION: {subscription.subscriber}")
        #Customer.objects.filter(id=customer_id).first()
        form = SubscriptionEditForm(instance=subscription)
        #print (f"Subscription_edit_view Subscription-id: {subscription_id}")
        return render(request, 'edit_subscription.html', {'form': form, 'subscription': subscription})


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
