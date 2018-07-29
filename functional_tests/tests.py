from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')

# assert 'To-Do' in browser.title

# browser.quit()

class NewVisitorTest(LiveServerTestCase):

	MAX_WAIT = 10

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def wait_for_row_in_list_table(self, row_text):
		# table = self.browser.find_element_by_id('id_list_table')
		# rows = self.browser.find_elements_by_tag_name('tr')
		# self.assertIn(row_text, [row.text for row in rows])

		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('id_list_table')
				rows = self.browser.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time-start_time>MAX_WAIT:
					raise e
				time.sleep(1)
		

	def test_can_start_a_list_and_retrieve_it_later(self):
		#有一个在线办事应用
		#去看了应用首页
		self.browser.get(self.live_server_url)
		# self.browser.get('http://localhost:8000')

		#注意到网站标题包含“To-Do”
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		#应用邀请他输入一个待办事项
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

		#她在一个文本框中输入“Buy peacock feathers”
		#她的爱好是使用假蝇做鱼饵钓鱼
		inputbox.send_keys('Buy peacock feather')

		#她按回车后页面更新
		#待办事项表格中显示了"1:Buy peacock feathers"
		inputbox.send_keys(Keys.ENTER)
		time.sleep(2) 
		self.wait_for_row_in_list_table('1:Buy peacock feather')


		# #页面中又显示了一个文本框，可以输入其他的待办事项
		# #她输入了“Use peacock feathers to make a fly”
		# #y伊迪斯做事很有条理
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(2)
		
		#页面再次刷新，清单中显示了这来两个事项
		# table = self.browser.find_element_by_id('id_list_table')
		# rows = table.find_elements_by_tag_name('tr')
		#self.assertTrue(any(row.text == '1:Buy peacock feathers' for row in rows),"New to-do item did not appear in table")
		# self.assertTrue(
		# 	any(row.text == '1:Buy peacock feathers' for row in rows), 
		# 	f"New to-do item did not in table.\n Content were:\n{table.text}"
		# 	)

		# self.assertIn('1:Buy peacock feathers', [row.text for row in rows])


		# table = self.browser.find_element_by_id('id_list_table')
		# rows = table.find_elements_by_tag_name('tr')
		# self.assertIn('1:Buy peacock feathers', [row.text for row in rows])
		# self.assertIn('2.Use peacock feathers to make a fl', [row.text for row in rows])


		self.wait_for_row_in_list_table('1:Buy peacock feather')
		self.wait_for_row_in_list_table('2:Use peacock feathers to make a fly')

		self.fail('Finish the Test!')



# if __name__ == '__main__':
# 	unittest.main(warnings='ignore')