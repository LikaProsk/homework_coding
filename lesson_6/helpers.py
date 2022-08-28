from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def check_element_on_page(web_driver, locator):
    try:
        WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(locator))
        return True
    except:
        return False


def get_elements(web_driver, locator):
    check_element(web_driver, locator)
    return web_driver.find_elements(locator[0], locator[1])


def get_element(web_driver, locator):
    check_element(web_driver, locator)
    return web_driver.find_element(locator[0], locator[1])


def get_element_by_name(web_driver, elements_locator, name_element):
    elements = get_elements(web_driver, elements_locator)

    result = None
    for element in elements:
        if element.text == name_element:
            result = element

    assert result is not None, f'Не удлось найти элемент с названием {name_element}'

    return result


def set_value_in_input(web_driver, locator, value):
    check_element(web_driver, locator)
    element = get_element(web_driver, locator)
    element.clear()
    element.send_keys(value)


def click_element_with_waiting(web_driver, locator):
    check_element(web_driver, locator)
    el = web_driver.find_element(locator[0], locator[1])
    el.click()


def check_element(web_driver, locator):
    check_result = check_element_on_page(web_driver, locator)
    assert check_result, f"Элемент {locator[1]} не найден"


def get_text_element(web_driver, locator):
    check_element(web_driver, locator)
    el = web_driver.find_element(locator[0], locator[1])
    return el.text


def check_elements(web_driver, locators):
    errors = []
    for locator in locators:
        result = check_element_on_page(web_driver, locator)
        if not result:
            errors.append(f'Элемент {locator[1]} не найден')

    assert not len(errors), '\n'.join(errors)
