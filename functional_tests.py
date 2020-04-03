from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    """Тест нового пользователя"""

    def setUp(self) -> None:
        """Установка"""
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        """демонтаж"""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_tater(self):
        """тест: можно начать список и получить его позже"""
        # Эдит слышала про новое крутое онлайн-приложение со списком
        # неотложных дел

        self.browser.get('http://localhost:8000')

        # Она видит, что заголовок и шапка говорят о списках
        # неотложных дел

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Ей сразу же предлагается ввести элемент списка
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # Она набирает в текстовом поле "Купить павлиньи перья" (её хобби
        # - вязание рыболовных мушек)
        inputbox.send_keys('Купить павлиньи перья')

        # Когда она нажымает Enter, страница обновляется, и теперь страница
        # содержит "1: Купить павлиньи перья" в качестве элемента списка
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Купить павлиньи перья', [row.text for row in rows],
                      f'Новый элемент списка не появился в таблице. Содержимым было \n {table.text}')

        # Текстовое поле по-прежнему приглашает её добавить ещё один элемент.
        # Она вводит "Сделать мушку из павлиньих переьев"
        # (Эдит очень методична)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих переьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Страница снова обновляется, и теперь показывает оба элемента её списка

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Купить павлиньи перья', [row.text for row in rows])
        self.assertIn('2: Сделать мушку из павлиньих переьев', [row.text for row in rows])

        # Эдит интересно, запомнит ли сайт её список. Далее она видит, что
        # сайт сгенерировал для неё уникальный URL-адрес - об этом
        # выводится небольшой текст с объявлением
        self.fail('Закончить тест!')

        # Она посещяет этот URL-адрес - её список по прежнему там.

        # Удовлетворённая, она снова ложится спать


if __name__ == '__main__':
    unittest.main(warnings='ignore')
