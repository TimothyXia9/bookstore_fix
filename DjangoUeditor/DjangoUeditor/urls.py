#coding:utf-8
from django import VERSION
# if VERSION[0:2]>(1,3):
#     from django.conf.urls import patterns, url
# else:
#     from django.conf.urls.defaults import patterns, url
from django.urls import path


from DjangoUeditor.views import get_ueditor_controller

urlpatterns = [
    path(r'^controller/$', get_ueditor_controller)
]
