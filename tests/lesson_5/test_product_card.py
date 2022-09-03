import allure

from lesson_6.page_object.home_page import HomePageObject
from lesson_6.page_object.list_products import ListProductsPageObject
from lesson_6.page_object.product_card import ProductCardPageObject


@allure.epic('Проверка карточек товаров')
class TestProductCard:

    @allure.story('Проверка открытия товара')
    def test_item(self, web_driver, log):
        home_page_object = HomePageObject(web_driver, log)
        list_products_page_object = ListProductsPageObject(web_driver, log)
        product_card_page_object = ProductCardPageObject(web_driver, log)
        home_page_object.click_element_menu_by_name('Tablets')
        product_name = 'Samsung Galaxy Tab 10.1'
        list_products_page_object.click_product_by_name(product_name)
        product_card_page_object.check_product_name(product_name)
