import allure

from selenium.webdriver.common.by import By

from lesson_6.helpers import get_element_by_name, set_value_in_input, click_element_with_waiting


class AddProductPageObject:

    def __init__(self, web_driver, log):
        self.log = log
        self.web_driver = web_driver

    tabs = (By.XPATH, "//form/ul[@class='nav nav-tabs']//a[@data-bs-toggle='tab']")
    button_save = (By.XPATH, "//button[@data-bs-original-title='Save']")

    fields_tab_general = {
        "Название товара": (By.ID, 'input-name-1'),
        "Title": (By.ID, 'input-meta-title-1')
    }

    fields_tab_data = {
        "Модель": (By.ID, "input-model")
    }

    @allure.step('Выбор вкладки {name}')
    def choose_tab_by_name(self, name):
        self.log.info(f'Выбор вкладки {name}')
        tab = get_element_by_name(self.web_driver, self.tabs, name)
        tab.click()
        self.log.info(f'Вкладка {name} выбрана')

    @allure.step('Ввод названия товара')
    def set_product_name(self, value):
        self.log.info(f'Ввод названия товара "{value}"')
        set_value_in_input(self.web_driver, self.fields_tab_general.get('Название товара'), value)
        self.log.info('Названия товара успешно введено')

    @allure.step('Ввод заголовка')
    def set_product_title(self, value):
        self.log.info(f'Ввод заголовка товара "{value}"')
        set_value_in_input(self.web_driver, self.fields_tab_general.get('Title'), value)
        self.log.info('Заголовок товара успешно введен')

    @allure.step('Ввод модели')
    def set_model(self, value):
        self.log.info(f'Ввод модели товара "{value}"')
        set_value_in_input(self.web_driver, self.fields_tab_data.get('Модель'), value)
        self.log.info('Модель товара успешно введено')

    @allure.step('Нажатие на кнопку сохранить')
    def click_button_save(self):
        self.log.info('Нажатие на кнопку сохранить')
        click_element_with_waiting(self.web_driver, self.button_save)
        self.log.info('Нажатие на кнопку сохранить прошло успешно')

    @allure.step('Создание товара')
    def add_product(self, name, title, model):
        self.log.info('Создание товара')
        self.set_product_name(name)
        self.set_product_title(title)
        self.choose_tab_by_name('Data')
        self.set_model(model)
        self.click_button_save()
        self.log.info('Товар создан')
