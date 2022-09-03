import allure

from selenium.webdriver.common.by import By

from lesson_6.helpers import get_text_element


class SuccessRegistrationPage:

    def __init__(self, web_driver, log):
        self.log = log
        self.web_driver = web_driver

    text_success_reg_el = (By.XPATH, '//div[@id="content"]//p[1]')

    text_success_reg = 'Поздравляем! Ваш Личный Кабинет был успешно создан.'

    @allure.step('Проверка сообщения об успешной регистрации')
    def check_text_success_reg(self):
        text_success_reg_el = get_text_element(self.web_driver, self.text_success_reg_el)
        assert text_success_reg_el == self.text_success_reg, 'Текущее сообщение не совпадает с ожидаемым.\n' \
                                                             f'Ожидалось: {self.text_success_reg}\n' \
                                                             f'Фактический результат: {text_success_reg_el}'
