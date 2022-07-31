import pytest
import requests as requests


def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="https://ya.ru", help="url сайта",
    )
    parser.addoption(
        "--status_code", action="store", default=200, help="статус код ответа",
    )


@pytest.fixture(scope='function')
def check_status_code(request):
    url = request.config.getoption('--url')
    status_code = request.config.getoption('--status_code')
    response = requests.get(url)

    return int(response.status_code) == int(status_code)
