from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user}"


class Bear(models.Model):
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(ProfileUser, on_delete=models.CASCADE, related_name='bears')
    price = models.FloatField()

    def __str__(self):
        return f"Brand: {self.brand}. Price: {self.price}"
