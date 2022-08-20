from selenium.webdriver.common.by import By

from lesson_6.helpers import check_elements, set_value_in_input, click_element_with_waiting


class RegistrationPageObject:

    def __init__(self, web_driver):
        self.web_driver = web_driver

    form_fields = {
        'Имя': (By.ID, 'input-firstname'),
        'Фамилия': (By.ID, 'input-lastname'),
        'email': (By.ID, 'input-email'),
        'Телефон': (By.ID, 'input-telephone'),
        'Пароль': (By.ID, 'input-password'),
        'Подтверждение пароля': (By.ID, 'input-confirm'),
        'Согласие': (By.NAME, 'agree'),
        'Продолжить': (By.XPATH, '//input[@type="submit"]'),
    }

    def open_page(self, url):
        self.web_driver.get(f'{url}//index.php?route=account/register')

    def check_form_elements(self):
        check_elements(self.web_driver, self.form_fields.values())

    def set_firstname(self, value):
        set_value_in_input(self.web_driver, self.form_fields.get('Имя'), value)

    def set_lastname(self, value):
        set_value_in_input(self.web_driver, self.form_fields.get('Фамилия'), value)

    def set_email(self, value):
        set_value_in_input(self.web_driver, self.form_fields.get('email'), value)

    def set_phone(self, value):
        set_value_in_input(self.web_driver, self.form_fields.get('Телефон'), value)

    def set_password(self, value):
        set_value_in_input(self.web_driver, self.form_fields.get('Пароль'), value)
        set_value_in_input(self.web_driver, self.form_fields.get('Подтверждение пароля'), value)

    def click_agree(self):
        click_element_with_waiting(self.web_driver, self.form_fields.get('Согласие'))

    def click_continue(self):
        click_element_with_waiting(self.web_driver, self.form_fields.get('Продолжить'))

    def registration(self, firstname, lastname, email, phone, password):
        self.set_firstname(firstname)
        self.set_lastname(lastname)
        self.set_email(email)
        self.set_phone(phone)
        self.set_password(password)
        self.click_agree()
        self.click_continue()
