from tests.lesson_5.base_test import BaseTest
from selenium.webdriver.common.by import By


class TestCatalog(BaseTest):

    def test_open_catalog(self, web_driver):
        tablets = 'Tablets'
        self.click_element_with_waiting(web_driver, (By.LINK_TEXT, tablets))
        category_title = (By.TAG_NAME, 'h2')
        result = self.check_element_on_page(web_driver, category_title)
        if result:
            text_element = self.get_text_element(web_driver, category_title)
            assert text_element == tablets, 'Заголовок страницы не совпадает с ожидаемым.\n' \
                                            f'Ожидалось: {tablets}\n' \
                                            f'Фактический результат: {text_element}'
