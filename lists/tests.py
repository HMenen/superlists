from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from lists.models import Item

# Create your tests here.

# class SmokeTest(TestCase):
# 	"""docstring for SmokeTest"""
	
# 	def test_bad_maths(self):
# 		self.assertEqual(1+1, 3)

class ItemModelTest(TestCase):

	def test_saving_and_retrieving_items(self):
		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.save()

		save_items = Item.objects.all()
		self.assertEqual(save_items.count(), 2)

		first_save_item = save_items[0]
		second_save_item = save_items[1]

		self.assertEqual(first_save_item.text, 'The first (ever) list item')
		self.assertEqual(second_save_item.text, 'Item the second')
		

class HomePageTest(TestCase):

	# def test_root_url_resolves_to_home_page_view(self):
	# 	found = resolve('/')
	# 	self.assertEqual(found.func, home_page)


	# def test_home_page_returns_correct_html(self):
	# 	# request = HttpRequest()
	# 	# response = home_page(request)
	# 	# html = response.content.decode('utf-8')
	# 	# self.assertTrue(html.startswith('<!DOCTYPE html>'))
	# 	# self.assertIn('<title>To-Do lists</title>', html)
	# 	# self.assertTrue(html.endswith('</html>'))
	# 	response = self.client.get('/')
	# 	html = response.content.decode('utf8')
	# 	self.assertTrue(html.startswith('<!DOCTYPE html>'))
	# 	self.assertIn('<title>To-Do lists</title>', html)
	# 	self.assertTrue(html.endswith('</html>'))

	def test_uses_home_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')


	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'item_text': 'A new list item'})
		# self.assertIn('A new list item', response.content.decode('utf8'))
		# self.assertTemplateUsed(response, 'home.html')

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new list item')

		# self.assertIn('A new list item', response.content.decode())
		# self.assertTemplateUsed(response, 'home.html')


	def test_redirect_after_POST(self):
		response = self.client.post('/', data={'item_text': 'A new list item'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')


	def test_displays_all_list_items(self):
		Item.objects.create(text='itemey 1')
		Item.objects.create(text="itemey 2")

		response = self.client.get('/')

		self.assertIn('itemey 1', response.content.decode())
		self.assertIn('itemey 2', response.content.decode())


	def test_only_save_items_when_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)







		












