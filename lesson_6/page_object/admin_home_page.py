from selenium.webdriver.common.by import By

from lesson_6.helpers import get_element_by_name


class AdminHomePage:

    def __init__(self, web_driver):
        self.web_driver = web_driver

    menu = (By.XPATH, '//ul[@id="menu"]/li/a')
    submenu = (By.XPATH, '//ul[@id="menu"]//ul[@class="collapse in"]/li/a')

    def click_category_menu_by_name(self, name):
        category = get_element_by_name(self.web_driver, self.menu, name)
        category.click()

    def click_subcategory_menu_by_name(self, name):
        subcategory = get_element_by_name(self.web_driver, self.submenu, name)
        subcategory.click()

    def check_title(self, title):
        page_title = self.web_driver.title
        assert page_title == title, 'Заголовок страницы не совпадает с ожидаемым.\n' \
                                    f'Ожидалось: {title}\n' \
                                    f'Фактический результат: {page_title}'
