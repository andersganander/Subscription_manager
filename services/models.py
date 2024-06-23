from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    # Make icon optional
    icon = models.CharField(max_length=200, blank=True)
    color = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.name}"


class Service(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=200, blank=True)
    default_price = models.IntegerField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name="service_categorys"
    )

    def __str__(self):
        return f"{self.name}"
