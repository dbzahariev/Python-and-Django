from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('profile/', views.redirect_to_user, name='user-redirect'),
    re_path('^profile/(?P<pk>\d+)/$', views.UserProfileDetails.as_view(), name='details'),
    path('', include('django.contrib.auth.urls')),
]
