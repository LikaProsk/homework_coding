from tests.lesson_5.base_test import BaseTest
from selenium.webdriver.common.by import By


class TestItemCard(BaseTest):

    def test_item(self, web_driver):
        tablets = 'Tablets'
        self.click_element_with_waiting(web_driver, (By.LINK_TEXT, tablets))
        item = (By.XPATH, "//div[@class='product-thumb']//h4")
        text_catalog_item = self.get_text_element(web_driver, item)
        self.click_element_with_waiting(web_driver, item)
        item_card_name = self.get_text_element(web_driver, (By.XPATH, '//div[@id="product-product"]//h1'))
        assert text_catalog_item == item_card_name, 'Наименование товара в каталоге и на карточке товара не ' \
                                                    'совпадают.\n' \
                                                    f'Ожидалось: {text_catalog_item}\n' \
                                                    f'Фактический результат: {item_card_name}'
