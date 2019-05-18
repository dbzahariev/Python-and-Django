from django.urls import path, include

from . import views

urlpatterns = [
    path('profile/', views),
    path('', include('django.contrib.auth.urls')),
]
