import allure

from selenium.webdriver.common.by import By

from lesson_6.helpers import check_elements, click_element_with_waiting, get_element_by_name, get_text_element


class HomePageObject:

    def __init__(self, web_driver, log):
        self.log = log
        self.web_driver = web_driver

    menu_currency = (By.XPATH, '//form[@id="form-currency"]//span')

    list_currency = (By.XPATH, "//form[@id='form-currency']//ul/li/button")

    currency = (By.XPATH, "//form[@id='form-currency']//strong")

    menu_element = {
        'Desktops': (By.LINK_TEXT, 'Desktops'),
        'Laptops & Notebooks': (By.LINK_TEXT, 'Laptops & Notebooks'),
        'Components': (By.LINK_TEXT, 'Components'),
        'Tablets': (By.LINK_TEXT, 'Tablets'),
        'Software': (By.LINK_TEXT, 'Software'),
        'Phones & PDAs': (By.LINK_TEXT, 'Phones & PDAs'),
        'Cameras': (By.LINK_TEXT, 'Cameras'),
        'MP3 Players': (By.LINK_TEXT, 'MP3 Players')
    }

    item_cards = {
        'MacBook': (By.LINK_TEXT, 'MacBook'),
        'iPhone': (By.LINK_TEXT, 'iPhone'),
        'Apple Cinema 30"': (By.LINK_TEXT, 'Apple Cinema 30"'),
        'Canon EOS 5D': (By.LINK_TEXT, 'Canon EOS 5D')
    }

    @allure.step('Получить текущую валюту')
    def get_current_currency(self):
        return get_text_element(self.web_driver, self.currency)

    @allure.step('Провека текущей валюты')
    def check_current_currency(self, currency):
        current_currency = self.get_current_currency()
        assert current_currency == currency, 'Текущая валюта не совпадает с ожидаемым.\n' \
                                             f'Ожидалось: {currency}\n' \
                                             f'Фактический результат: {current_currency}'

    @allure.step('Выбор валюты {currency_name}')
    def change_currency_by_name(self, currency_name):
        click_element_with_waiting(self.web_driver, self.menu_currency)
        currency = get_element_by_name(self.web_driver, self.list_currency, currency_name)
        currency.click()

    @allure.step('Проверка наличия элементов меню')
    def check_menu_element(self):
        check_elements(self.web_driver, self.menu_element.values())

    @allure.step('Проверка наличия элементов товаров')
    def check_item_cards_elements(self):
        check_elements(self.web_driver, self.item_cards.values())

    @allure.step('Выбор пункта меню по названию')
    def click_element_menu_by_name(self, name_element):
        assert name_element in self.menu_element.keys(), 'Не получилось найти локатор для элемента с названием' \
                                                         f' {name_element} из списка \n {self.menu_element}'

        click_element_with_waiting(self.web_driver, self.menu_element.get(name_element))
