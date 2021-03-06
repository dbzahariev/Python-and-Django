from django.db import models

# Create your models here.


class Animal(models.Model):
    KIND_CHOICES = (
        ('D', 'Dog'),
        ('C', 'Cat')
    )
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    bread = models.CharField(max_length=20)
    description = models.TextField()
    image_url = models.URLField()
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)

    def __str__(self):
        return f'{self.name} and I am {self.age}'
