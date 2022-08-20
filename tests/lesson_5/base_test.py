from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseTest:

    def check_element_on_page(self, web_driver, element):
        try:
            WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(element))
            return True
        except:
            return False

    def click_element_with_waiting(self, web_driver, element):
        result = self.check_element_on_page(web_driver, element)
        assert result, f"Элемент {element[1]} не найден"
        el = web_driver.find_element(element[0], element[1])
        el.click()

    def get_text_element(self, web_driver, element):
        result = self.check_element_on_page(web_driver, element)
        assert result, f"Элемент {element[1]} не найден"
        el = web_driver.find_element(element[0], element[1])
        return el.text
