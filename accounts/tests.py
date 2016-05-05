#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#File Name: test.py
#Copyright(c) 2015-2024 Beijing Carryon.top Corp.
#
#Author LiuBin on:" Wed Apr 27 17:19:10 CST 2016
#
#@desc:
#
#@history
#


from django.test import TestCase
from django.test.utils import setup_test_environment
from django.test import Client
from django.core.urlresolvers import reverse, resolve

from accounts.models import User
from accounts import views

# Create your tests here.
setup_test_environment()
client = Client()

class UserMethodTest(TestCase):
    def test_is_staff(self):
        """
        should return False if user's is_staff value is not 1
        """
        user = User(is_staff = 0)
        self.assertEqual(user.is_staff, False)


class UserViewTest(TestCase):
    def test_index_view_template(self):
        input_url = '/'
        url = reverse('accounts:index')
        found = resolve(url)
        response = self.client.get(input_url)

        # 测试url解析是否正确
        self.assertEqual(input_url, url)
        # 测试服务器响应是否正确
        self.assertEqual(response.status_code, 200)
        # 测试调用的视图类或函数是否正确
        #self.assertEqual(found.func, views.IndexView.as_view)
        # 测试视图类或函数调用的模板是否正确
        self.assertTemplateUsed(response, 'accounts/index.html')
        # 测试视图类或函数调用的模板内容是否正确
        self.assertContains(response, "index view")
        

    def test_index_view_without_login(self):
        """
        If not login, login link should be displayed.
        """
        input_url = '/'
        url = reverse('accounts:index')
        found = resolve(url)
        response = self.client.get(input_url)

        # 测试url解析是否正确
        self.assertEqual(input_url, url)
        # 测试服务器响应是否正确
        self.assertEqual(response.status_code, 200)
        # 测试调用的视图类或函数是否正确
        #self.assertEqual(found.func, views.IndexView.get)
        # 测试视图类或函数调用的模板是否正确
        self.assertTemplateUsed(response, 'accounts/index.html')
        # 测试视图类或函数调用的模板内容是否正确
        self.assertContains(response, "login")
        self.assertNotContains(response, "logout")

    def test_user_add_view(self):
        """
        Test if user add view show OK.
        """
        #self.assertIsInstance(response.context['form'], LoginForm)
        

        #self.assertRedirects(response, reverse('accounts:login'))
        #self.assertEqual(response.context['latest_user_list'], [])
        # 确认跳转的URL正确
        #self.assertEqual(response.location, '/')
