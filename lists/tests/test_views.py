from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from lists.models import Item, List
import os


class ListAndItemModelsTest(TestCase):
	def test_saving_and_retrieving_items(self):
		list_ = List()
		list_.save()

		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.list = list_
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.list = list_
		second_item.save()

		save_list = List.objects.first()
		self.assertEqual(save_list, list_)

		save_items = Item.objects.all()
		self.assertEqual(save_items.count(), 2)

		first_save_item = save_items[0]
		second_save_item = save_items[1]

		self.assertEqual(first_save_item.text, 'The first (ever) list item')
		self.assertEqual(second_save_item.text, 'Item the second')
		self.assertEqual(first_save_item.list, list_)
		self.assertEqual(second_save_item.list, list_)








