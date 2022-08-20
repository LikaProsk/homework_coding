from lesson_6.page_object.home_page import HomePageObject
from lesson_6.page_object.list_products import ListProductsPageObject


class TestListProducts:

    def test_open_catalog(self, web_driver):
        name_category = 'Tablets'
        home_page_object = HomePageObject(web_driver)
        list_products_page_object = ListProductsPageObject(web_driver)
        home_page_object.click_element_menu_by_name(name_category)
        list_products_page_object.check_title_page(name_category)
