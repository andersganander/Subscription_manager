from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscriptions_view, name='subscription_list'),
    path('add/', views.subscription_form_view, name='subscription_form'),
    path('edit/<int:subscription_id>',views.subscription_edit_view, name='subscription_edit'),
    path('delete/<int:subscription_id>/', views.subscription_delete_view, name='subscription_delete'),
    path('summary/', views.subscriptions_summary_view, name='subscription_summary'),
    path('about/', views.about_view, name='about'),
]
