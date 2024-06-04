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
        fields = ['active', 'monthly_price', 'subscription_category', 'notes', 'reminder_date', 'reminder_notes' ]
        widgets = {
            'active': forms.Select(attrs={'class': 'browser-default'}, choices=[[True,'Yes'],[False,'No']]),
            'monthly_price': forms.NumberInput(attrs={'class': 'validate'}),
            'notes': forms.TextInput(attrs={'class': 'validate'}),
            'reminder_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'reminder_notes': forms.TextInput(attrs={'class': 'validate'}),
            'subscription_category': forms.Select(attrs={'class': 'browser-default'}), 
        }

        # 'active': forms.NullBooleanSelect(attrs={'class': 'browser-default'}),