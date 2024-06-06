import json
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

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
    context = {'subscriptions' : subscriptions}
    #return HttpResponse("<h1>Subscriptions</h1>")
    return render(request, 'subscription_list.html', context)

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