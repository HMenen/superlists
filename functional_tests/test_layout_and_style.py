from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
from .base import FunctionalTest



class LayoutAndStylingTest(FunctionalTest):
	def test_layout_and_style(self):
		#伊迪斯访问首页
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024, 768)

		#她看到输入框完美居中显示
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(inputbox.location['x']+inputbox.size['width']/2, 512, delta=10)

		inputbox.send_keys('testing')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1:testing')
		self.assertAlmostEqual(inputbox.location['x']+inputbox.size['width']/2, 512, delta=10)

	