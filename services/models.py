from django.db import models

# Create your models here.
  
  
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    
    # Add validation to check if it's an FA icon
    icon = models.CharField(max_length=200, help_text='Add the name of the Font Awesome icon')
    
    # Change to color picker
    # https://mackenzie.morgan.name/posts/django-admin-color-picker/
    color = models.CharField(max_length=50)
