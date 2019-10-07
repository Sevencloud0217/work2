
from django.urls import path,include,re_path
from BookGuan.views import *
urlpatterns = [
    path('register/',register),
    path('login/',login),
    path('index/',index),
    path('logout/',logout),
    path('base/',base),
    path('goods_list/',goods_list),
    re_path("goods_list/(?P<status>[01])/(?P<page>\d+)/", goods_list),
    re_path("goods_status/(?P<status>\w+)/(?P<id>\d+)/", goods_status),
    path('goods_add/', goods_add),
    # path('personal_info/', personal_info),
]