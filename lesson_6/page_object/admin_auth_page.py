import allure

from selenium.webdriver.common.by import By
from lesson_6.helpers import check_elements, set_value_in_input, click_element_with_waiting


class AdminAuthPageObject:

    def __init__(self, web_driver, log):
        self.log = log
        self.web_driver = web_driver

    form_elements = {
        'Логин': (By.ID, 'input-username'),
        'Пароль': (By.ID, 'input-password'),
        'Войти': (By.TAG_NAME, 'button')
    }

    @allure.step('Открытие страницы админки')
    def open_page(self, url):
        page = f'{url}/admin'
        self.log.info(f'Открытие страницы {page}')
        self.web_driver.get(page)
        self.log.info(f'Cтраница {page} успешно открыта')

    @allure.step('Проверка наличия элементов формы авторизации')
    def check_form_elements(self):
        self.log.info('Проверка наличия элементов формы авторизации')
        check_elements(self.web_driver, self.form_elements.values())
        self.log.info('Все элементы успешно найдены')

    @allure.step('Заполнене поля логин')
    def set_login(self, login):
        self.log.info(f'Заполнене поля логин "{login}"')
        set_value_in_input(self.web_driver, self.form_elements.get('Логин'), login)
        self.log.info('Поле успешно заполнено')

    @allure.step('Заполнене поля пароль')
    def set_password(self, password):
        self.log.info(f'Заполнене поля пароль "{password}"')
        set_value_in_input(self.web_driver, self.form_elements.get('Пароль'), password)
        self.log.info('Поле успешно заполнено')

    @allure.step('Нажатие на кнопку войти')
    def click_enter(self):
        self.log.info('Нажатие на кнопку войти')
        click_element_with_waiting(self.web_driver, self.form_elements.get('Войти'))
        self.log.info('Кнопка успешно нажата')

    @allure.step('Авторизация')
    def authorize(self, login, password):
        self.log.info('Авторизация')
        self.set_login(login)
        self.set_password(password)
        self.click_enter()
        self.log.info('Авторизация прошла успешно')

