from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.BearList.as_view(), name='ListBears'),
    re_path('^details/(?P<pk>\d+)/$', views.BearDetails.as_view(), name='bear-detail'),
    re_path('mine/', views.UserBears.as_view(), name='user-bears')
]
