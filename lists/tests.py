from django.test import TestCase
from django.urls import resolve

from lists.views import home_page
from lists.models import Item


class HomePageTest(TestCase):
    """Тест домашней страницы"""

    def test_root_url_resolves_to_home_page_view(self):
        """тест: корневой url преобразуется в представление
         домашней страницы"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_uses_home_template(self):
        """тест: используется домашний шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        """тест: можно сохранить post-запрос"""
        self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirect_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_display_all_list_items(self):
        """тест: отображаются все элементы списка"""
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        responce = self.client.get('/')

        self.assertIn('itemey 1', responce.content.decode())
        self.assertIn('itemey 2', responce.content.decode())


class ItemModelTest(TestCase):
    """тест модели элемента списка"""

    def test_saving_and_retrieving_items(self):
        """тест сохраниения и получения элементов списка"""
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
