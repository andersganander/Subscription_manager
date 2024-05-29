from django.shortcuts import render
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