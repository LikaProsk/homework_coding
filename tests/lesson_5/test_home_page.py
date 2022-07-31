from tests.lesson_5.base_test import BaseTest
from selenium.webdriver.common.by import By


class TestHomePage(BaseTest):

    def test_wait_elements_home_page(self, web_driver):
        elements = [
            (By.LINK_TEXT, 'Desktops'),
            (By.LINK_TEXT, 'Desktops'),
            (By.LINK_TEXT, 'Laptops & Notebooks'),
            (By.LINK_TEXT, 'Components'),
            (By.LINK_TEXT, 'Tablets'),
            (By.LINK_TEXT, 'Software'),
            (By.LINK_TEXT, 'Phones & PDAs'),
            (By.LINK_TEXT, 'Cameras'),
            (By.LINK_TEXT, 'MP3 Players'),
            (By.LINK_TEXT, 'MacBook'),
            (By.LINK_TEXT, 'iPhone'),
            (By.LINK_TEXT, 'Apple Cinema 30"'),
            (By.LINK_TEXT, 'Apple Cinema 30"')
        ]

        errors = []
        for element in elements:
            result = self.check_element_on_page(web_driver, element)
            if not result:
                errors.append(f'Элемент {element[1]} не найден')

        assert not len(errors), '\n'.join(errors)
