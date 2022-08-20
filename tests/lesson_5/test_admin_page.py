import random

from lesson_6.page_object.add_product_page import AddProductPageObject
from lesson_6.page_object.admin_auth_page import AdminAuthPageObject
from lesson_6.page_object.admin_home_page import AdminHomePage
from lesson_6.page_object.admin_list_products import AdminListProductsPageObject


class TestAdminPage:
    name_new_product = f'Товар {random.randint(10, 10000)}'

    def test_wait_elements_admin_page(self, web_driver, url):
        admin_auth_page = AdminAuthPageObject(web_driver)
        admin_auth_page.open_page(url)
        admin_auth_page.check_form_elements()

    def test_admin_auth(self, web_driver, url):
        admin_auth_page = AdminAuthPageObject(web_driver)
        admin_home_page = AdminHomePage(web_driver)
        admin_auth_page.open_page(url)
        admin_auth_page.authorize('demo', 'demo')
        admin_home_page.check_title('Панель состояния')

    def test_add_product(self, web_driver, url):
        admin_auth_page = AdminAuthPageObject(web_driver)
        admin_home_page = AdminHomePage(web_driver)
        admin_list_products_page = AdminListProductsPageObject(web_driver)
        add_product_page = AddProductPageObject(web_driver)
        admin_auth_page.open_page(url)
        admin_auth_page.authorize('demo', 'demo')
        admin_home_page.check_title('Панель состояния')
        admin_home_page.click_category_menu_by_name('Каталог')
        admin_home_page.click_subcategory_menu_by_name('Товары')
        admin_list_products_page.click_button_add_product()
        add_product_page.add_product(self.name_new_product, self.name_new_product, 'Product 15')

    def test_delete_product(self, web_driver, url):
        admin_auth_page = AdminAuthPageObject(web_driver)
        admin_home_page = AdminHomePage(web_driver)
        admin_list_products_page = AdminListProductsPageObject(web_driver)
        admin_auth_page.open_page(url)
        admin_auth_page.authorize('demo', 'demo')
        admin_home_page.check_title('Панель состояния')
        admin_home_page.click_category_menu_by_name('Каталог')
        admin_home_page.click_subcategory_menu_by_name('Товары')
        admin_list_products_page.delete_product(self.name_new_product)
