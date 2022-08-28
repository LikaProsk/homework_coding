from selenium.webdriver.common.by import By
from lesson_6.helpers import check_elements, set_value_in_input, click_element_with_waiting


class AdminAuthPageObject:

    def __init__(self, web_driver):
        self.web_driver = web_driver

    form_elements = {
        'Логин': (By.ID, 'input-username'),
        'Пароль': (By.ID, 'input-password'),
        'Войти': (By.TAG_NAME, 'button')
    }

    def open_page(self, url):
        self.web_driver.get(f'{url}/admin')

    def check_form_elements(self):
        check_elements(self.web_driver, self.form_elements.values())

    def set_login(self, login):
        set_value_in_input(self.web_driver, self.form_elements.get('Логин'), login)

    def set_password(self, password):
        set_value_in_input(self.web_driver, self.form_elements.get('Пароль'), password)

    def click_enter(self):
        click_element_with_waiting(self.web_driver, self.form_elements.get('Войти'))

    def authorize(self, login, password):
        self.set_login(login)
        self.set_password(password)
        self.click_enter()
