from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve
from django.http import HttpResponse

from lists.views import home_page


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
