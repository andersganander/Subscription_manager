from django import forms
from .models import Service, Subscription

class SubscriptionForm(forms.ModelForm):
    
    class Meta:
        model = Subscription
        fields = 'service', 'monthly_price','expiry_date'
    

class SubscriptionEditForm(forms.ModelForm):
    
    class Meta:
        model = Subscription
        fields = '__all__'
