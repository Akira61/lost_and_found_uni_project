from django.conf import settings
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=255, blank=True)
    is_dropoff_point = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='user')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class LostItem(models.Model):
    STATUS_CHOICE = [
        ('O', 'OPEN'),
        ('C', 'CLOSE')
    ]

    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category')
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='user')
    photo = models.ImageField(upload_to='items/')
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=True, blank=True)
    dropoff_point = models.ForeignKey(Location, on_delete=models.PROTECT)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='O')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Claim(models.Model):
    pass
