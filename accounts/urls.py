#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#File Name: urls.py
#Copyright(c) 2015-2024 Beijing Carryon.top Corp.
#
#Author LiuBin on:" Wed Apr 27 17:56:41 CST 2016
#
#@desc:
#
#@history
#

from django.conf.urls import url
from accounts import views 

urlpatterns = [
    url(r'^test$', views.MyView.as_view(), name='test'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'user/add/$', views.UserCreate.as_view(), name='user_add'),
    url(r'user/(?P<pk>[0-9]+)/$', views.UserUpdate.as_view(), name='user_update'),
    url(r'user/(?P<pk>[0-9]+)/delete$', views.UserDelete.as_view(), name='user_delete'),
    url(r'users/$', views.UserList.as_view(), name='user_list'),
]

