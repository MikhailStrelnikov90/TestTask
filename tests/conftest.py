import pytest
import requests
from requests import Response
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from typing import NoReturn
import os
import allure
from .pages.main_page import MainPage
from .api.users_api import UsersAPI
from .api.resourse_api import ResourceAPI
from pyvirtualdisplay import Display

if os.environ.get("ENVIRONMENT") != 'local':
    display = Display(visible=False, size=(1920, 1080))
    display.start()


def pytest_addoption(parser) -> NoReturn:
    parser.addoption('--browser', action='store', default="chrome", help="Choose browser: chrome or firefox")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        try:
            if 'browser' in item.fixturenames:
                browser = item.funcargs['browser']
            else:
                return
            allure.attach(
                browser.get_screenshot_as_png(),
                name='Screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screenshot: {}'.format(e))


@pytest.fixture(scope="function")
def browser(request):
    browser = None
    browser_name = request.config.getoption("browser")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        if os.environ.get("ENVIRONMENT") != 'local':
            options.add_argument("start-maximized")
            options.add_argument("disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")
            browser = webdriver.Chrome(options=options)
        else:
            browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        browser.maximize_window()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        if os.environ.get("ENVIRONMENT") != 'local':
            browser = webdriver.Firefox()
            browser.set_window_size(1920, 1080)
        else:
            browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            browser.maximize_window()
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    browser.quit()


class ApiClient:

    def __init__(self, base_address) -> None:
        self.base_address: str = base_address

    @allure.step('Making GET request to "{path}"')
    def get_request(self, path="/", params=None, headers=None) -> Response:
        url: str = f"{self.base_address}{path}"
        return requests.get(url=url, params=params, headers=headers)

    @allure.step('Making POST request to "{path}"')
    def post_request(self, path="/", params=None, data=None, json=None, headers=None) -> Response:
        url: str = f"{self.base_address}{path}"
        return requests.post(url=url, params=params, data=data, json=json, headers=headers)

    @allure.step('Making DELETE request to "{path}"')
    def delete_request(self, path="/", params=None, headers=None) -> Response:
        url: str = f"{self.base_address}{path}"
        return requests.delete(url=url, params=params, headers=headers)

    @allure.step('Making PUT request to "{path}"')
    def put_request(self, path="/", params=None, data=None, json=None, headers=None) -> Response:
        url: str = f"{self.base_address}{path}"
        return requests.put(url=url, params=params, data=data, json=json, headers=headers)

    @allure.step('Making PATCH request to "{path}"')
    def patch_request(self, path="/", params=None, data=None, json=None, headers=None) -> Response:
        url: str = f"{self.base_address}{path}"
        return requests.patch(url=url, params=params, data=data, json=json, headers=headers)


@pytest.fixture
def api_reqres() -> ApiClient:
    return ApiClient(base_address="https://reqres.in/")


@pytest.fixture
def main_page(browser, api_reqres) -> MainPage:
    return MainPage(browser, api_reqres)


@pytest.fixture
def users_api(api_reqres) -> UsersAPI:
    return UsersAPI(api_reqres)


@pytest.fixture
def resource_api(api_reqres) -> ResourceAPI:
    return ResourceAPI(api_reqres)
