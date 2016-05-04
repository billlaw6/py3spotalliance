#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#File Name: models.py
#Copyright(c) 2015-2024 Beijing Carryon.top Corp.
#
#Author LiuBin on:" Wed Apr 27 16:47:42 CST 2016
#
#@desc:
#
#@history
#

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
    扩展auth模块的类，在settings中设置AUTH_USER_MODEL替换默认的User类。
    """
    mobile = models.CharField(_('mobile'), max_length=11, unique=True, null=True, blank=True, db_index=True)
    avatar = models.ImageField(_('avatar'), upload_to='accounts/avatar', blank=True, null=True, max_length=100)
    sex = models.PositiveSmallIntegerField(_('sex'), default=1)
    uid = models.CharField(_('uid'), max_length=50, null=True, blank=True)
    access_token = models.CharField(_('access_token'), max_length=100, null=True, blank=True)
    url = models.URLField(_('url'), unique=True, null=True, blank=True)
    desc = models.CharField(_('desc'), max_length=2000, null=True, blank=True)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

    @models.permalink
    def get_absolute_url(self):
        return ('user_profile',(),{'username':self.username})


