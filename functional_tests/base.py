from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException


MAX_WAIT = 10

class FunctionalTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def wait_for_row_in_list_table(self, row_text):
		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('id_list_table')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time()-start_time>MAX_WAIT:
					raise e
				time.sleep(1)



	def wait_for(self, row_text):
		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('id_list_table')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time()-start_time>MAX_WAIT:
					raise e
				time.sleep(1)
		


