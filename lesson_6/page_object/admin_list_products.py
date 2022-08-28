import allure

from selenium.webdriver.common.by import By

from lesson_6.helpers import get_elements, click_element_with_waiting


class AdminListProductsPageObject:

    def __init__(self, web_driver, log):
        self.log = log
        self.web_driver = web_driver

    list_product = (By.XPATH, "//tbody//tr")
    product_checkbox = (By.XPATH, "//tr//td/input[@type='checkbox']")
    button_delete = (By.XPATH, "//bytton[@data-bs-original-title='Delete']")
    button_add = (By.XPATH, "//a[@data-bs-original-title='Add New']")

    @allure.step('Выбор товара из списка по имени')
    def choose_product_in_list_by_name(self, name):
        self.log.info(f'Выбор товара "{name}" из списка')
        products = get_elements(self.web_driver, self.list_product)

        result = None
        index = 0
        for product in products:
            product_name = product.text
            index += 1
            if name in product_name:
                result = product
                break

        if result is None:
            self.log.error(f'Неудалось найти товар с именем {name}')
        assert result is not None, f'Неудалось найти товар с именем {name}'
        product_checkbox = result.find_element(self.product_checkbox[0], f"//tr[{index}]//td/input[@type='checkbox']")
        product_checkbox.click()
        self.log.info('Выбор товара из списка по имени успешно произошел')

    @allure.step('Проверка наличия товара в списке')
    def check_product_in_table_by_name(self, name):
        self.log.info(f'Проверка наличия товара "{name}" в списке')
        products = get_elements(self.web_driver, self.list_product)

        result = False
        for product in products:
            product_name = product.text
            if name in product_name:
                result = True
                self.log.info(f'Товар "{name}" найден в списке')
                break
        if not result:
            self.log.error('Товар не найден')
        return result

    @allure.step('Нажатие на кнопку удалить товар')
    def click_button_delete(self):
        self.log.info('Нажатие на кнопку удалить товар')
        click_element_with_waiting(self.web_driver, self.button_delete)
        self.log.info('Нажатие на кнопку удалить товар прошло успешно')

    @allure.step('Удаление товара')
    def delete_product(self, name):
        self.log.info('Удаление товара')
        self.choose_product_in_list_by_name(name)
        self.click_button_delete()
        if self.check_product_in_table_by_name(name):
            self.log.error(f'Товар {name} не удален')
        else:
            self.log.info('Товар успешно удален')
        assert not self.check_product_in_table_by_name(name), f'Товар {name} не удален'

    @allure.step('Нажатие на кнопку добавить товар')
    def click_button_add_product(self):
        self.log.info('Нажатие на кнопку добавить товар')
        click_element_with_waiting(self.web_driver, self.button_add)
        self.log.info('Нажатие на кнопку добавить товар успешно прошло')

