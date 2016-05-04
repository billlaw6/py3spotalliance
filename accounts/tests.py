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
from django.core.urlresolvers import reverse

from accounts.models import User

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
    def test_index_view_with_no_user(self):
        """
        If no user exist, an appropriate message shold be displayed.
        """

        response = self.client.get(reverse('accounts:index'))

        self.assertEqual(response.status_code, '302')
        self.assertContains(response, "user index")
        self.assertUsersetEqual(response.context['latest_user_list'], [])

    def test_user_add_view(self):
        """
        Test if user add view show OK.
        """
        

