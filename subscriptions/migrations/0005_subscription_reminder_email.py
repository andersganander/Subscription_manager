# Generated by Django 5.0.6 on 2024-06-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_alter_subscription_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='reminder_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
