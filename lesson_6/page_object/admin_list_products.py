from selenium.webdriver.common.by import By

from lesson_6.helpers import get_elements, click_element_with_waiting


class AdminListProductsPageObject:

    def __init__(self, web_driver):
        self.web_driver = web_driver

    list_product = (By.XPATH, "//tbody//tr")
    product_checkbox = (By.XPATH, "//tr//td/input[@type='checkbox']")
    button_delete = (By.XPATH, "//bytton[@title='Удалить']")
    button_add = (By.XPATH, "//a[@data-original-title='Добавить']")

    def choose_product_in_list_by_name(self, name):
        products = get_elements(self.web_driver, self.list_product)

        result = None
        index = 0
        for product in products:
            product_name = product.text
            index += 1
            if name in product_name:
                result = product
                break

        assert result is not None, f'Неудалось найти товар с именем {name}'
        product_checkbox = result.find_element(self.product_checkbox[0], f"//tr[{index}]//td/input[@type='checkbox']")
        product_checkbox.click()

    def check_product_in_table_by_name(self, name):
        products = get_elements(self.web_driver, self.list_product)

        result = False
        for product in products:
            product_name = product.text
            if name in product_name:
                result = True
                break

        return result

    def click_button_delete(self):
        click_element_with_waiting(self.web_driver, self.button_delete)

    def delete_product(self, name):
        self.choose_product_in_list_by_name(name)
        self.click_button_delete()
        assert not self.check_product_in_table_by_name(name), f'Товар {name} не удален'

    def click_button_add_product(self):
        click_element_with_waiting(self.web_driver, self.button_add)
