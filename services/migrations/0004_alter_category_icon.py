# Generated by Django 5.0.6 on 2024-06-20 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_service_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
