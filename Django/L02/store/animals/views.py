from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Animal

# Create your views here.


def serialized_data(data):
    try:
        return serialize('json', data)
    except:
        return serialize('json', [data])


def get_all_animals(request):
    name = request.GET.get('name')
    if name:
        animal = Animal.objects.all().filter(name=name)
        return HttpResponse(serialized_data(animal))
    animals = Animal.objects.all()
    return HttpResponse(serialized_data(animals))


def get_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return HttpResponse(serialized_data(animal))


def get_all_dogs(request):
    dogs = Animal.objects.filter(kind='D', age='6', bread='Yorkie')
    return HttpResponse(serialized_data(dogs))


def order_animals(request):
    animals = Animal.objects.all().order_by('-name')
    return HttpResponse(serialized_data(animals))
