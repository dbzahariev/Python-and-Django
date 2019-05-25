from django.urls import path, re_path

from . import views

urlpatterns = [
    # path('', views.BearList.as_view(), name='ListBears'),
    path('', views.Bears.as_view(), name='ListBears'),
    re_path(r'^(?P<pk>\d+)/$', views.BearDetail.as_view())
    # re_path('^details/(?P<pk>\d+)/$', views.BearDetails.as_view(), name='bear-detail'),
    # re_path('mine/', views.UserBears.as_view(), name='user-bears')
]
