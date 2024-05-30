from django.shortcuts import render
from django.contrib import messages
from services.models import Service
from .forms import SubscriptionForm
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
    return render(request, 'list.html', context)

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
    else:
        form = SubscriptionForm()

    return render(request, 'add_subscription.html', {'form': form})