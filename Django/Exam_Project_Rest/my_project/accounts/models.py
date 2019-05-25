from django.contrib.auth.models import User
from django.core import validators
from django.db import models

from . import enum


# Create your models here.
class Alcoholic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(validators=[validators.MinValueValidator(18)])
    gender = models.CharField(max_length=15, choices=[(g.name, g.value) for g in enum.GenderEnum],
                              default=enum.GenderEnum.M)

    def __str__(self):
        return f'Alcoholic {self.user} ({self.gender}).'
