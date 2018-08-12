# from selenium import webdriver
# import unittest
# from selenium.webdriver.common.keys import Keys
# import time
# from django.test import LiveServerTestCase
# from selenium.common.exceptions import WebDriverException
# from unittest import skip


# MAX_WAIT = 10

# class FunctionalTest(LiveServerTestCase):
# 	def setUp(self):
# 		self.browser = webdriver.Firefox()

# 	def tearDown(self):
# 		self.browser.quit()

# 	def wait_for_row_in_list_table(self, row_text):
# 		start_time = time.time()
# 		while True:
# 			try:
# 				table = self.browser.find_element_by_id('id_list_table')
# 				rows = table.find_elements_by_tag_name('tr')
# 				self.assertIn(row_text, [row.text for row in rows])
# 				return
# 			except (AssertionError, WebDriverException) as e:
# 				if time.time()-start_time>MAX_WAIT:
# 					raise e
# 				time.sleep(1)
		



# class NewVisitorTest(FunctionalTest):

# 	def test_can_start_a_list_and_retrieve_it_later(self):
# 		#有一个在线办事应用
# 		#去看了应用首页
# 		self.browser.get(self.live_server_url)

		
# 		#应用邀请他输入一个待办事项
# 		inputbox = self.browser.find_element_by_id('id_new_item')
# 		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to do item')

# 		#她在一个文本框中输入“Buy peacock feathers”
# 		#她的爱好是使用假蝇做鱼饵钓鱼
# 		inputbox.send_keys('Buy peacock feather')

# 		#她按回车后页面更新
# 		#待办事项表格中显示了"1:Buy peacock feathers"
# 		inputbox.send_keys(Keys.ENTER)
# 		self.wait_for_row_in_list_table('1:Buy peacock feather')


# 		# #页面中又显示了一个文本框，可以输入其他的待办事项
# 		# #她输入了“Use peacock feathers to make a fly”
# 		# #y伊迪斯做事很有条理
# 		inputbox = self.browser.find_element_by_id('id_new_item')
# 		inputbox.send_keys('Use peacock feathers to make a fly')
# 		inputbox.send_keys(Keys.ENTER)

# 		self.wait_for_row_in_list_table('2:Use peacock feathers to make a fly')
# 		self.wait_for_row_in_list_table('1:Buy peacock feather')

# 		# self.fail('Finish the Te bst!')


# 	def test_can_start_a_list_one_user(self):
# 		#有一个在线办事应用
# 		#去看了应用首页
# 		self.browser.get(self.live_server_url)
		
# 		#应用邀请他输入一个待办事项
# 		#她在一个文本框中输入“Buy peacock feathers”
# 		#她的爱好是使用假蝇做鱼饵钓鱼
# 		inputbox = self.browser.find_element_by_id('id_new_item')
# 		inputbox.send_keys('Buy peacock feather')
# 		inputbox.send_keys(Keys.ENTER)
# 		self.wait_for_row_in_list_table('1:Buy peacock feather')
# 		#页面中又显示了一个文本框，可以输入其他的待办事项
# 		#她输入了“Use peacock feathers to make a fly”
# 		#伊迪斯做事很有条理
# 		inputbox = self.browser.find_element_by_id('id_new_item')
# 		inputbox.send_keys('Use peacock feathers to make a fly')
# 		inputbox.send_keys(Keys.ENTER)

# 		#页面再次刷新，清单中显示了这来两个事项
# 		self.wait_for_row_in_list_table('2:Use peacock feathers to make a fly')
# 		self.wait_for_row_in_list_table('1:Buy peacock feather')
		

# 	def test_multiple_users_can_start_lists_at_different_urls(self):
# 		#伊迪斯新建一个待办事项 
# 		self.browser.get(self.live_server_url)
# 		inputbox = self.browser.find_element_by_id('id_new_item')
# 		inputbox.send_keys('Buy peacock feathers')
# 		inputbox.send_keys(Keys.ENTER)
# 		self.wait_for_row_in_list_table('1:Buy peacock feathers')

# 		#她注意到清单有个唯一的url
# 		edith_list_url = self.browser.current_url
# 		self.assertRegex(edith_list_url, '/lists/.+')


# 		#现在一名叫做弗朗西斯的新用户访问了网站

# 		##使用一个新的会话
# 		##确保弗朗西斯的信息不回从cookie中泄露出去
# 		self.browser.quit()
# 		self.browser = webdriver.Firefox()

# 		#弗朗西斯访问首页
# 		#页面中看不到伊迪斯的清单
# 		self.browser.get(self.live_server_url)
# 		page_text = self.browser.find_element_by_tag_name('body').text
# 		self.assertNotIn('Buy peacock feathers', page_text)
# 		self.assertNotIn('make a fly', page_text)

# 		#弗朗西斯输入一个新待办事项，新建一个清单
# 		#他没有伊迪斯那样兴趣盎然
# 		inputbox = self.browser.find_element_by_id('id_new_item')
# 		inputbox.send_keys('Buy milk')
# 		inputbox.send_keys(Keys.ENTER)
# 		self.wait_for_row_in_list_table('1:Buy milk')

# 		#弗朗西斯获得了唯一URL
# 		francis_list_url = self.browser.current_url
# 		self.assertRegex(francis_list_url, '/lists/.+')
# 		self.assertNotEqual(francis_list_url, edith_list_url)

# 		#这个页面还是没有伊迪斯的清单内容
# 		page_text = self.browser.find_element_by_tag_name('body').text
# 		self.assertNotIn('Buy peacock feather', page_text)
# 		self.assertIn('Buy milk', page_text)


# 		#两人都很满意，然后休息去了


# class LayoutAndStylingTest(FunctionalTest):
# 	def test_layout_and_style(self):
# 		#伊迪斯访问首页
# 		self.browser.get(self.live_server_url)
# 		self.browser.set_window_size(1024, 768)

# 		#她看到输入框完美居中显示
# 		inputbox = self.browser.find_element_by_id('id_new_item')
# 		self.assertAlmostEqual(inputbox.location['x']+inputbox.size['width']/2, 512, delta=10)

# 		inputbox.send_keys('testing')
# 		inputbox.send_keys(Keys.ENTER)
# 		self.wait_for_row_in_list_table('1:testing')
# 		self.assertAlmostEqual(inputbox.location['x']+inputbox.size['width']/2, 512, delta=10)

	


# class ItemValidationTest(FunctionalTest):
	
# 	@skip
# 	def test_cannot_add_empty_list_item(self):
# 		#伊迪斯访问首页，不小心提交了一个空待办事项
# 		pass