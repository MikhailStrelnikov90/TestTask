import allure
from typing import NoReturn
import json
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser, url: str, api_reqres=None) -> None:
        self.browser = browser
        self.url = url
        self.api_reqres = api_reqres

    main_page_url: str = "https://reqres.in/"

    @staticmethod
    def create_screenshot(func):
        def wrapper(*args, **kwargs):
            self = args[0]
            func(*args, **kwargs)
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        return wrapper

    @create_screenshot
    def open(self) -> NoReturn:
        self.browser.get(self.url)

    def reload(self) -> NoReturn:
        self.browser.refresh()

    def go_to_first_window(self) -> NoReturn:
        self.browser.switch_to.window(self.browser.window_handles[0])

    def go_to_second_window(self) -> NoReturn:
        self.browser.switch_to.window(self.browser.window_handles[1])

    def go_to_third_window(self) -> NoReturn:
        self.browser.switch_to.window(self.browser.window_handles[2])

    def waiting_element_and_click_with_scroll(self, element_for_scroll: tuple, element: tuple) -> NoReturn:
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", self.browser.find_element(*element_for_scroll))
        WebDriverWait(self.browser, timeout=30).until(EC.element_to_be_clickable(element)).click()

    def clear_element(self, element: tuple) -> NoReturn:
        WebDriverWait(self.browser, timeout=20).until(EC.element_to_be_clickable(element)).clear()

    def element_send_keys(self, element: tuple, data) -> NoReturn:
        self.browser.find_element(*element).send_keys(data)

    def waiting_element_to_visible(self, element: tuple) -> NoReturn:
        WebDriverWait(self.browser, timeout=30).until(EC.visibility_of_element_located(element))

    def waiting_element_to_invisible(self, element: tuple) -> NoReturn:
        WebDriverWait(self.browser, timeout=30).until(EC.invisibility_of_element_located(element))

    def scroll_to_element(self, element: tuple) -> NoReturn:
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", self.browser.find_element(*element))

    @staticmethod
    def create_attachment(message: str, name_attach: str) -> NoReturn:
        allure.attach(message, name=name_attach, attachment_type=AttachmentType.JSON)

    def is_element_present(self, element: tuple) -> bool:
        try:
            self.browser.find_element(*element)
        except NoSuchElementException:
            return False
        return True

    def assert_status_code(self, expected_status_code: tuple, status_code_from_request: int) -> NoReturn:
        self.waiting_element_to_visible(expected_status_code)
        assert self.is_element_present(expected_status_code)
        assert self.get_attribute(expected_status_code) == str(status_code_from_request)

    def assert_response_body(self, expected_response_body: tuple, response_body_from_request: dict) -> NoReturn:
        self.waiting_element_to_visible(expected_response_body)
        assert self.is_element_present(expected_response_body)
        assert json.loads(self.get_attribute(expected_response_body)) == response_body_from_request

    def assert_response_body_with_changing_values(self, expected_response_body: tuple, response_body_from_request: dict) -> NoReturn:
        self.waiting_element_to_visible(expected_response_body)
        assert self.is_element_present(expected_response_body)
        assert json.loads(self.get_attribute(expected_response_body)).keys() == response_body_from_request.keys()

    def get_attribute(self, element: tuple) -> str:
        return self.browser.find_element(*element).text
