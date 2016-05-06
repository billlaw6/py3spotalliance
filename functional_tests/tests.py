#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
#File Name: ".expand("%"))
#Copyright(c) 2015-2024 Beijing Carryon.top Corp.
#
#Author LiuBin on:" Thu Apr 28 20:54:08 EDT 2016
#
#@desc:
#
#@history
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.FireFox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.bowser.quit()

    def test_interactive_func(self):
        # 用户访问首页
        self.browser.get('http://localhost:8000')

        self.assertIn('index', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Index', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Test input content')

        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: alsdk' for row in rows)
        )

        self.fail('Finish the test')

    if __name__ == '__main__':
        unittest.main(warnings='ignore')


