from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    
    # Add validation to check if it's an FA icon
    icon = models.CharField(max_length=200, help_text='Add the name of the Font Awesome icon')
    
    # Change to color picker
    # https://mackenzie.morgan.name/posts/django-admin-color-picker/
    color = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.name}"

class Service(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=200, blank=True)
    default_price = models.IntegerField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name="services"
    )

    def __str__(self):
        return f"{self.name}"
  
