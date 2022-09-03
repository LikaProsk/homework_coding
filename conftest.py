import os
import allure
import pytest
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService

from lesson_7.logging_helper import LoggingHelper


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://demo.opencart.com", help="url сайта"
                     )
    parser.addoption("--status_code", action="store", default=200, help="статус код ответа"
                     )
    parser.addoption("--browser", action="store", default="chrome", help="браузер для запуска")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--drivers", action="store", default="lesson_5/drivers", help="путь до webdriver")


@pytest.fixture()
def test_name(request):
    return request.function.__name__


@pytest.fixture(scope='function')
def check_status_code(request):
    url = request.config.getoption('--url')
    status_code = request.config.getoption('--status_code')
    response = requests.get(url)

    return int(response.status_code) == int(status_code)


@pytest.fixture()
def web_driver(request, url):
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    executor = request.config.getoption("--executor")

    if executor == 'localhost' or executor == '127.0.0.1':
        if browser == "chrome":
            service = ChromiumService(executable_path=get_root_dir() + "/" + drivers + "/chromedriver")
            driver = webdriver.Chrome(service=service)
        elif browser == "firefox":
            service = FFService(executable_path=drivers + "/geckodriver")
            driver = webdriver.Firefox(service=service)
        elif browser == "opera":
            driver = webdriver.Opera(executable_path=drivers + "/operadriver")
        else:
            driver = webdriver.Safari()
    else:
        executor_url = f'http://{executor}:4444/wd/hub'
        caps = {
            'browserName': browser
        }
        driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)
    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver


def get_root_dir():
    return os.path.dirname(__file__)


@pytest.fixture()
def log(test_name):
    return LoggingHelper(get_root_dir(), test_name).log()


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'web_driver' in item.fixturenames:
                    web_driver = item.funcargs['web_driver']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
