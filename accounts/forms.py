#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#File Name: ".expand("%"))
#Copyright(c) 2015-2024 Beijing Carryon.top Corp.
#
#Author LiuBin on:" Wed Apr 27 22:57:04 CST 2016
#
#@desc:
#
#@history
#

from django import forms
from django.utils.translation import ugettext_lazy as _
from accounts.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', ]
        # 使用model构建form尽量使用下面的widgets参数，这样能继承model中已有的属性，如help_text, max_length等
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
        }

    #override the default __init__ so we can set the request
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(UserForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(UserForm, self).clear()
        return self.cleaned_data


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', ]
        # 使用model构建form尽量使用下面的widgets参数，这样能继承model中已有的属性，如help_text, max_length等
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
        }

    #override the default __init__ so we can set the request
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(UserForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(UserForm, self).clear()
        return self.cleaned_data


