import os

import pytest
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://demo-opencart.ru", help="url сайта"
                     )
    parser.addoption("--status_code", action="store", default=200, help="статус код ответа"
                     )
    parser.addoption("--browser", action="store", default="chrome", help="браузер для запуска")
    parser.addoption("--drivers", action="store", default="lesson_5/drivers", help="путь до webdriver")


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

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver


def get_root_dir():
    return os.path.dirname(__file__)


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")
