import random

from lesson_6.page_object.registration_page import RegistrationPageObject
from lesson_6.page_object.success_registration_page import SuccessRegistrationPage


class TestRegisterPage:

    def test_wait_elements_register_page(self, web_driver, url):
        registration_page_object = RegistrationPageObject(web_driver)
        registration_page_object.open_page(url)
        registration_page_object.check_form_elements()

    def test_registration(self, web_driver, url):
        registration_page_object = RegistrationPageObject(web_driver)
        success_registration_page = SuccessRegistrationPage(web_driver)
        registration_page_object.open_page(url)
        registration_page_object.registration('Лилия', 'Проскурина', f'test{random.randint(100,1000)}@gmail.com', '89111111111', 'qazwsx1234')
        success_registration_page.check_text_success_reg()
