from tests.lesson_5.base_test import BaseTest
from selenium.webdriver.common.by import By


class TestRegisterPage(BaseTest):

    def test_wait_elements_register_page(self, web_driver, url):
        web_driver.get(f'{url}//index.php?route=account/register')

        elements = [
            ('поле Основные данные', (By.CSS_SELECTOR, '#account>legend')),
            ('поле Имя', (By.ID, 'input-firstname')),
            ('поле Пароль', (By.CSS_SELECTOR, 'fieldset:nth-child(2)>legend'))
        ]

        errors = []
        for element in elements:
            result = self.check_element_on_page(web_driver, element[1])
            if not result:
                errors.append(f'Элемент {element[0]} {element[1][1]} не найден')

        assert not len(errors), '\n'.join(errors)
