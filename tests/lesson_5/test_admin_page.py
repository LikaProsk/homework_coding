import random
import allure
from lesson_6.page_object.add_product_page import AddProductPageObject
from lesson_6.page_object.admin_auth_page import AdminAuthPageObject
from lesson_6.page_object.admin_home_page import AdminHomePage
from lesson_6.page_object.admin_list_products import AdminListProductsPageObject


@allure.epic('Проверка админки')
class TestAdminPage:
    name_new_product = f'Товар {random.randint(10, 10000)}'

    @allure.story('Проверка наличия элементов на странице авторизации')
    def test_wait_elements_admin_page(self, web_driver, url, log):
        admin_auth_page = AdminAuthPageObject(web_driver, log)
        admin_auth_page.open_page(url)
        admin_auth_page.check_form_elements()

    @allure.story('Проверка авторизации')
    def test_admin_auth(self, web_driver, url, log):
        admin_auth_page = AdminAuthPageObject(web_driver, log)
        admin_home_page = AdminHomePage(web_driver, log)
        admin_auth_page.open_page(url)
        admin_auth_page.authorize('demo', 'demo')
        admin_home_page.check_title('Administration')

    @allure.story('Проверка добавления товара')
    def test_add_product(self, web_driver, url, log):
        admin_auth_page = AdminAuthPageObject(web_driver, log)
        admin_home_page = AdminHomePage(web_driver, log)
        admin_list_products_page = AdminListProductsPageObject(web_driver, log)
        add_product_page = AddProductPageObject(web_driver, log)
        admin_auth_page.open_page(url)
        admin_auth_page.authorize('demo', 'demo')
        admin_home_page.check_title('Administration')
        admin_home_page.close_modal_window()
        admin_home_page.click_category_menu_by_name('Catalog')
        admin_home_page.click_subcategory_menu_by_name('Products')
        admin_list_products_page.click_button_add_product()
        add_product_page.add_product(self.name_new_product, self.name_new_product, 'Product 15')

    @allure.story('Проверка удаления товара')
    def test_delete_product(self, web_driver, url, log):
        admin_auth_page = AdminAuthPageObject(web_driver, log)
        admin_home_page = AdminHomePage(web_driver, log)
        admin_list_products_page = AdminListProductsPageObject(web_driver, log)
        admin_auth_page.open_page(url)
        admin_auth_page.authorize('demo', 'demo')
        admin_home_page.check_title('Administration')
        admin_home_page.close_modal_window()
        admin_home_page.click_category_menu_by_name('Catalog')
        admin_home_page.click_subcategory_menu_by_name('Products')
        admin_list_products_page.delete_product(self.name_new_product)
