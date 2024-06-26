from django.db import models
from django.contrib.auth.models import User
from services.models import Service, Category

# Create your models here.


class Subscription(models.Model):
    monthly_price = models.IntegerField()
    notes = models.CharField(max_length=200, blank=True)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)
    service = models.ForeignKey(
        Service, on_delete=models.RESTRICT,
        related_name="subscription"
    )
    subscription_name = models.CharField(max_length=100)

    subscriber = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="subscriptions"
    )

    subscription_category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL,
        related_name="subscription_categorys"
    )
    reminder_email = models.EmailField(max_length=254, blank=True)
    reminder_date = models.DateField(blank=True, null=True)
    reminder_notes = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.subscriber.username} : {self.subscription_name}"

    class Meta:
        unique_together = ('subscription_name', 'subscriber',)
