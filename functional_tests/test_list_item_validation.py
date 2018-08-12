from selenium import webdriver
from unittest import skip
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
	
	# @unittest.skip("直接跳过")
	def test_cannot_add_empty_list_item(self):
		#伊迪斯访问首页，不小心提交了一个空待办事项
		self.browser.get(self.live_server_url)
		self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

		#首页刷新了，显示一个错误消息
		#提示待办事项不能为空
		self.wait_for(lambda: self.assertEqual(
			self.browser.find_element_by_css_selector('.has-error').text,
			"You can't have an empty list item"
			))

		# #她输入一些文字，然后再次提交，这次么问题了
		# self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
		# self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
		# self.wait_for_row_in_list_table('1:Buy milk')

		# #她又输入了一个空的待办事项
		# self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

		# #她在列表页面看到了一条类似的错误信息
		# self.wait_for(lambda: assertEqual(
		# 		self.browser.find_element_by_css_selector('.has-error').text,
		# 		"You can't have an empty list item"
		# 	))

		# #输入文字之后就没问题了
		# self.browser.find_element_by_id('id_new_item').send_keys('Make tea')
		# self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
		# self.wait_for_row_in_list_table('1:Buy tea')
		# self.wait_for_row_in_list_table('2:Make tea')













