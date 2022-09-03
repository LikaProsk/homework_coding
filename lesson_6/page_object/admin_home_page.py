import allure
from selenium.webdriver.common.by import By

from lesson_6.helpers import get_element_by_name, click_element_with_waiting


class AdminHomePage:

    def __init__(self, web_driver, log):
        self.log = log
        self.web_driver = web_driver

    menu = (By.XPATH, '//ul[@id="menu"]/li/a')
    submenu = (By.XPATH, '//ul[@id="menu"]//ul[@class="collapse show"]/li/a')
    button_close_modal = (By.XPATH, '//button[@data-bs-dismiss="modal"]')

    @allure.step('Открытие категории {name}')
    def click_category_menu_by_name(self, name):
        self.log.info(f'Открытие категории {name}')
        category = get_element_by_name(self.web_driver, self.menu, name)
        category.click()
        self.log.info(f'Категория {name} открыта')

    @allure.step('Открытие подкатегории {name}')
    def click_subcategory_menu_by_name(self, name):
        self.log.info(f'Открытие подкатегории {name}')
        subcategory = get_element_by_name(self.web_driver, self.submenu, name)
        subcategory.click()
        self.log.info(f'Подкатегория {name} открыта')

    @allure.step('Закрыть модальное окно')
    def close_modal_window(self, ):
        self.log.info('Закрыть модальное окно')
        click_element_with_waiting(self.web_driver, self.button_close_modal)
        self.log.info('Модальное окно закрыто')

    @allure.step('Проверка заголовка страницы')
    def check_title(self, title):
        self.log.info(f'Проверка заголовка страницы {title}')
        page_title = self.web_driver.title

        if page_title != title:
            self.log.error('Заголовок страницы не совпадает с ожидаемым.\n'
                           f'Ожидалось: {title}\n'
                           f'Фактический результат: {page_title}')

        assert page_title == title, 'Заголовок страницы не совпадает с ожидаемым.\n' \
                                    f'Ожидалось: {title}\n' \
                                    f'Фактический результат: {page_title}'
