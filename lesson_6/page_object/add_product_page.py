from selenium.webdriver.common.by import By

from lesson_6.helpers import get_element_by_name, set_value_in_input, click_element_with_waiting


class AddProductPageObject:

    def __init__(self, web_driver):
        self.web_driver = web_driver

    tabs = (By.XPATH, "//form/ul[@class='nav nav-tabs']//a[@data-toggle='tab']")
    button_save = (By.XPATH, "//button[@data-original-title='Сохранить']")

    fields_tab_general = {
        "Название товара": (By.ID, 'input-name1'),
        "Title": (By.ID, 'input-meta-title1')
    }

    fields_tab_data = {
        "Модель": (By.ID, "input-model")
    }

    def choose_tab_by_name(self, name):
        tab = get_element_by_name(self.web_driver, self.tabs, name)
        tab.click()

    def set_product_name(self, value):
        set_value_in_input(self.web_driver, self.fields_tab_general.get('Название товара'), value)

    def set_product_title(self, value):
        set_value_in_input(self.web_driver, self.fields_tab_general.get('Title'), value)

    def set_model(self, value):
        set_value_in_input(self.web_driver, self.fields_tab_data.get('Модель'), value)

    def click_button_save(self):
        click_element_with_waiting(self.web_driver, self.button_save)

    def add_product(self, name, title, model):
        self.set_product_name(name)
        self.set_product_title(title)
        self.choose_tab_by_name('Данные')
        self.set_model(model)
        self.click_button_save()
