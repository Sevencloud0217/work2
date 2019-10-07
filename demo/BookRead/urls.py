from django.urls import path,include,re_path
from BookRead.views import *
urlpatterns = [
    path('login/',login),
    path("register/",register),
    path("index/",index),
    path("base/",base),
    path('listpic/',listpic),
    path('about/',about),
    path('newslistpic/',newslistpic),
    re_path('newslistpic/(?P<page>\d+)',newslistpic),
    re_path('xiangxi/(?P<id>\d+)',xiangxi),
]