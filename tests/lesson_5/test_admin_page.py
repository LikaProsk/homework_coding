from tests.lesson_5.base_test import BaseTest
from selenium.webdriver.common.by import By


class TestAdminPage(BaseTest):

    def test_wait_elements_admin_page(self, web_driver, url):
        web_driver.get(f'{url}/admin')

        elements = [
            ('поле Логин', (By.ID, 'input-username')),
            ('поле Пароль', (By.ID, 'input-password')),
            ('кнопка Войти', (By.TAG_NAME, 'button'))
        ]

        errors = []
        for element in elements:
            result = self.check_element_on_page(web_driver, element[1])
            if not result:
                errors.append(f'Элемент {element[0]} {element[1][1]} не найден')

        assert not len(errors), '\n'.join(errors)
