#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#File Name: ".expand("%"))
#Copyright(c) 2015-2024 Beijing Carryon.top Corp.
#
#Author LiuBin on:" Wed Apr 27 17:07:53 CST 2016
#
#@desc:自定义登录验证后台，支持手机、邮箱和用户名三种方式登录
#
#@history
#

import re

from accounts.models import User

class LoginBackend(object):
    def authenticate(self, username=None, password=None):
        if username:
            #email 
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", username) != None: 
                print("Email auth!\n")
                try:
                    user = User.objects.get(email=username) 
                    if user.check_password(password):
                        return user 
                except User.DoesNotExist:
                    return None
            #mobile
            elif len(username)==11 and re.match("^(1[3458]\d{9})$", username) != None:
                print("Mobile auth!\n")
                try: 
                    user = User.objects.get(mobile=username) 
                    if user.check_password(password): 
                        return user 
                except User.DoesNotExist: 
                    return None  
            #nick 
            else: 
                print("Nickname auth!\n")
                try: 
                    user = User.objects.get(username=username) 
                    if user.check_password(password): 
                        return user 
                except User.DoesNotExist: 
                    return None
        else: 
            return None 
            
    def get_user(self, user_id): 
        try: 
            return User.objects.get(pk=user_id)
        except User.DoesNotExist: 
            return None 

