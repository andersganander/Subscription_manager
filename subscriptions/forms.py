from django import forms
from .models import Service, Subscription

class SubscriptionForm(forms.ModelForm):
    
    class Meta:
        model = Subscription
        fields = 'service', 'monthly_price','expiry_date'
    

# class SubscriptionEditForm(forms.ModelForm):
    
#     class Meta:
#         model = Subscription
#         fields = '__all__'


class SubscriptionEditForm(forms.ModelForm):
   
    class Meta:
        model = Subscription
        fields = ['monthly_price', 'notes', 'expiry_date', 'active', 'service', 'subscriber', 'subscription_reminder', 'paymentmethod', 'subscription_category']
        widgets = {
            'monthly_price': forms.NumberInput(attrs={'class': 'validate'}),
            'notes': forms.Textarea(attrs={'class': 'materialize-textarea'}),
            'expiry_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'datepicker'}),
            'active': forms.CheckboxInput(),
            'paymentmethod': forms.TextInput(attrs={'class': 'validate'}),
        }
