from django.shortcuts import render
from django.http import HttpResponse
 
 
def subscriptions(request):
  return HttpResponse("<h1>Subscriptions</h1>")