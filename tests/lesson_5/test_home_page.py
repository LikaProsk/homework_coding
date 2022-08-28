from lesson_6.page_object.home_page import HomePageObject


class TestHomePage:

    def test_wait_elements_home_page(self, web_driver):
        self.home_page_object = HomePageObject(web_driver)
        self.home_page_object.check_menu_element()
        self.home_page_object.check_item_cards_elements()

    def test_change_currency(self, web_driver):
        self.home_page_object = HomePageObject(web_driver)
        self.home_page_object.change_currency_by_name('$ US Dollar')
        self.home_page_object.check_current_currency('$')
