from django import forms
from .models import Service, Subscription

class SubscriptionForm(forms.ModelForm):
    
    class Meta:
        model = Subscription
        fields = 'service', 'monthly_price','expiry_date'
    
    # service_name = forms.ModelChoiceField(queryset=Service.objects.all().order_by('name'), label="Service Name")
    # price = forms.IntegerField(label="Price")
