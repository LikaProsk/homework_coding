from selenium.webdriver.common.by import By

from lesson_6.helpers import get_text_element


class ProductCardPageObject:

    def __init__(self, web_driver):
        self.web_driver = web_driver

    product_name = (By.XPATH, '//div[@id="product-product"]//h1')

    def check_product_name(self, product_name):
        name = get_text_element(self.web_driver, self.product_name)
        assert name == product_name, 'Наименование товара в каталоге и на карточке товара не ' \
                                     'совпадают.\n' \
                                     f'Ожидалось: {name}\n' \
                                     f'Фактический результат: {product_name}'
