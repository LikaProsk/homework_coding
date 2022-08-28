from selenium.webdriver.common.by import By

from lesson_6.helpers import get_text_element, get_element_by_name


class ListProductsPageObject:

    def __init__(self, web_driver):
        self.web_driver = web_driver

    products = (By.XPATH, "//div[@class='product-thumb']//h4")
    category_title = (By.TAG_NAME, 'h2')

    def get_product_element_by_name(self, name_product):
        return get_element_by_name(self.web_driver, self.products, name_product)

    def click_product_by_name(self, name_product):
        product = self.get_product_element_by_name(name_product)
        product.click()

    def check_title_page(self, title):
        category_title = get_text_element(self.web_driver, self.category_title)
        assert category_title == title, 'Назваание категории товатора не совпадает с ожидаемым.\n' \
                                        f'Ожидалось: {title}\n' \
                                        f'Фактический результат: {category_title}'
