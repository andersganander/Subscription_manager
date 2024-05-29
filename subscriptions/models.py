from django.db import models
from django.contrib.auth.models import User
from services.models import Service, Category

# Create your models here.

# TODO Update ERD 
class Reminder(models.Model):
    message = models.CharField(max_length=200)
    reminder_date = models.DateField()

class Subscription(models.Model):
    monthly_price = models.IntegerField()
    notes = models.TextField(blank=True)
    expiry_date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)
    service = models.ForeignKey(
        Service, on_delete=models.RESTRICT,
        related_name="subscription"
    )
    subscriber = models.ForeignKey(
        User, on_delete = models.CASCADE,
        related_name="subscriptions"
    )
    subscription_reminder = models.ForeignKey(
        Reminder, null=True, on_delete = models.SET_NULL,
        related_name="reminder"
    )
    paymentmethod = models.CharField(max_length=200, blank=True)
    subscription_category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL,
        related_name="subscription_categorys"
    )

    def __str__(self):
        return f"{self.subscriber.username : self.service.name}"
