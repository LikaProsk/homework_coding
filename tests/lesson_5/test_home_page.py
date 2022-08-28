import allure
from lesson_6.page_object.home_page import HomePageObject


@allure.epic('Проверка главной страницы')
class TestHomePage:

    @allure.story('Проверка наличия элементов на домашней странице')
    def test_wait_elements_home_page(self, web_driver, log):
        self.home_page_object = HomePageObject(web_driver, log)
        self.home_page_object.check_menu_element()
        self.home_page_object.check_item_cards_elements()

    @allure.story('Проверка изменения валюты')
    def test_change_currency(self, web_driver, log):
        self.home_page_object = HomePageObject(web_driver, log)
        self.home_page_object.change_currency_by_name('$ US Dollar')
        self.home_page_object.check_current_currency('$')
