from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
 
def services(request):
  return render(request, 'service.html')
  #return HttpResponse("<h1>Services</h1>")