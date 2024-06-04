from django import forms
from .models import Service, Subscription

class SubscriptionForm(forms.ModelForm):
    
    class Meta:
        model = Subscription
        fields = 'service', 'monthly_price'
    

# class SubscriptionEditForm(forms.ModelForm):
    
#     class Meta:
#         model = Subscription
#         fields = '__all__'


class SubscriptionEditForm(forms.ModelForm):
   
    class Meta:
        model = Subscription
        fields = ['monthly_price', 'notes', 'active', 'service', 'subscriber', 'subscription_category']
        widgets = {
            'monthly_price': forms.NumberInput(attrs={'class': 'validate'}),
            'notes': forms.TextInput(attrs={'class': 'validate'}),
            'active': forms.CheckboxInput(),
        }