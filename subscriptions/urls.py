from django.urls import path
#now import the views.py file into this code
from . import views

urlpatterns = [
    path('', views.subscriptions_view, name='subscription_list'),
    path('add/', views.subscription_form_view, name='subscription_form'),

]