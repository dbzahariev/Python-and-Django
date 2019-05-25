from django.contrib.auth.models import User
from django.db import models


# from my_project.accounts.models import Alcoholic
# from my_project.my_project import enum

# Create your models here.
class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user}"


class Bear(models.Model):
    # Brand = models.CharField(max_length=15, choices=[(b.name, b.value) for b in enum.BearBrandEnum])
    color = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(ProfileUser, on_delete=models.CASCADE, related_name='bears', blank=True)
    price = models.FloatField()

    def __str__(self):
        return f"Brand: ({self.owner}). Price: {self.price}"
