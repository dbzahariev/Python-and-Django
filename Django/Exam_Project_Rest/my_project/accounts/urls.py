from django.urls import path, include

urlpatterns = [
    path('', include('rest_auth.urls')),
    # path('register/', views.RegisterUser.as_view(), name='register')
]
