from typing import NoReturn
from .base_page import BasePage
from tests.api.users_api import UsersAPI
from tests.api.resourse_api import ResourceAPI
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser, api_reqres) -> None:
        self.users_api = UsersAPI(api_reqres)
        self.resource_api = ResourceAPI(api_reqres)
        super().__init__(browser, BasePage.main_page_url, api_reqres)

    @BasePage.create_screenshot
    def click_on_user(self, request_name: str) -> NoReturn:
        if request_name == 'list_users':
            self.waiting_element_and_click_with_scroll(MainPageLocators.RESPONSE_STATUS, MainPageLocators.SELECT_LIST_USERS)
        elif request_name == 'single_user':
            self.waiting_element_and_click_with_scroll(MainPageLocators.RESPONSE_STATUS, MainPageLocators.SELECT_SINGLE_USER)
        elif request_name == 'single_user_not_found':
            self.waiting_element_and_click_with_scroll(MainPageLocators.RESPONSE_STATUS, MainPageLocators.SELECT_SINGLE_USER_NOT_FOUND)

    @BasePage.create_screenshot
    def click_on_resource(self, request_name: str) -> NoReturn:
        if request_name == 'list_resource':
            self.waiting_element_and_click_with_scroll(MainPageLocators.RESPONSE_STATUS, MainPageLocators.SELECT_LIST_RESOURCE)
        elif request_name == 'single_resource':
            self.waiting_element_and_click_with_scroll(MainPageLocators.RESPONSE_STATUS, MainPageLocators.SELECT_SINGLE_RESOURCE)
        elif request_name == 'single_resource_not_found':
            self.waiting_element_and_click_with_scroll(MainPageLocators.RESPONSE_STATUS, MainPageLocators.SELECT_SINGLE_RESOURCE_NOT_FOUND)

    @BasePage.create_screenshot
    def click_on_edit_user(self, request_name: str) -> NoReturn:
        if request_name == 'Create user':
            self.waiting_element_and_click_with_scroll(MainPageLocators.RESPONSE_STATUS, MainPageLocators.SELECT_CREATE_USER)
        elif request_name == 'Update (PUT) user':
            self.waiting_element_and_click_with_scroll(MainPageLocators.RESPONSE_STATUS, MainPageLocators.SELECT_UPDATE_PUT_USER)
        elif request_name == 'Update (PATCH) user':
            self.waiting_element_and_click_with_scroll(MainPageLocators.RESPONSE_STATUS, MainPageLocators.SELECT_UPDATE_PATCH_USER)
        elif request_name == 'Delete user':
            self.waiting_element_and_click_with_scroll(MainPageLocators.RESPONSE_STATUS, MainPageLocators.SELECT_DELETE_USER)

    @BasePage.create_screenshot
    def click_on_register_user(self, request_name: str) -> NoReturn:
        if request_name == 'Register successful':
            self.waiting_element_and_click_with_scroll(MainPageLocators.RESPONSE_STATUS, MainPageLocators.SELECT_REGISTER_SUCCESSFUL_USER)
        elif request_name == 'Register unsuccessful':
            self.waiting_element_and_click_with_scroll(MainPageLocators.RESPONSE_STATUS, MainPageLocators.SELECT_REGISTER_UNSUCCESSFUL_USERS)

    @BasePage.create_screenshot
    def click_on_login_user(self, request_name: str) -> NoReturn:
        if request_name == 'Login successful':
            self.waiting_element_and_click_with_scroll(MainPageLocators.RESPONSE_STATUS, MainPageLocators.SELECT_LOGIN_SUCCESSFUL_USER)
        elif request_name == 'Login unsuccessful':
            self.waiting_element_and_click_with_scroll(MainPageLocators.RESPONSE_STATUS, MainPageLocators.SELECT_LOGIN_UNSUCCESSFUL_USER)

    @BasePage.create_screenshot
    def click_on_delayed_response(self) -> NoReturn:
        self.waiting_element_and_click_with_scroll(MainPageLocators.RESPONSE_STATUS, MainPageLocators.SELECT_DELAYED_RESPONSE)

    @BasePage.create_screenshot
    def should_be_status_code_and_body_equal_api_get_users(self, request_name: str, user_id: int) -> NoReturn:
        if request_name == 'list_users':
            self.assert_status_code(MainPageLocators.RESPONSE_STATUS, self.users_api.list_users(user_id).status)
            self.assert_response_body(MainPageLocators.RESPONSE_BODY, self.users_api.list_users(user_id).response)
        elif request_name == 'single_user':
            self.assert_status_code(MainPageLocators.RESPONSE_STATUS, self.users_api.single_users(user_id).status)
            self.assert_response_body(MainPageLocators.RESPONSE_BODY, self.users_api.single_users(user_id).response)
        elif request_name == 'single_user_not_found':
            self.assert_status_code(MainPageLocators.RESPONSE_STATUS, self.users_api.single_users(user_id).status)
            self.assert_response_body(MainPageLocators.RESPONSE_BODY, self.users_api.single_users(user_id).response)

    @BasePage.create_screenshot
    def should_be_status_code_and_body_equal_api_get_resource(self, request_name: str, resource_id: int) -> NoReturn:
        if request_name == 'list_resource':
            self.assert_status_code(MainPageLocators.RESPONSE_STATUS, self.resource_api.list_resource().status)
            self.assert_response_body(MainPageLocators.RESPONSE_BODY, self.resource_api.list_resource().response)
        elif request_name == 'single_resource':
            self.assert_status_code(MainPageLocators.RESPONSE_STATUS, self.resource_api.single_resource(resource_id).status)
            self.assert_response_body(MainPageLocators.RESPONSE_BODY, self.resource_api.single_resource(resource_id).response)
        elif request_name == 'single_resource_not_found':
            self.assert_status_code(MainPageLocators.RESPONSE_STATUS, self.resource_api.single_resource(resource_id).status)
            self.assert_response_body(MainPageLocators.RESPONSE_BODY, self.resource_api.single_resource(resource_id).response)

    @BasePage.create_screenshot
    def should_be_status_code_and_body_equal_api_edit_user(self, request_name: str, name: str, job: str, user_id: int) -> NoReturn:
        if request_name == 'Create user':
            self.assert_status_code(MainPageLocators.RESPONSE_STATUS, self.users_api.create_user(name, job).status)
            self.assert_response_body_with_changing_values(MainPageLocators.RESPONSE_BODY, self.users_api.create_user(name, job).response)
        elif request_name == 'Update (PUT) user':
            self.assert_status_code(MainPageLocators.RESPONSE_STATUS, self.users_api.update_user("PUT", user_id, name, job).status)
            self.assert_response_body_with_changing_values(MainPageLocators.RESPONSE_BODY, self.users_api.update_user("PUT", user_id, name, job).response)
        elif request_name == 'Update (PATCH) user':
            self.assert_status_code(MainPageLocators.RESPONSE_STATUS, self.users_api.update_user("PATCH", user_id, name, job).status)
            self.assert_response_body_with_changing_values(MainPageLocators.RESPONSE_BODY, self.users_api.update_user("PATCH", user_id, name, job).response)
        elif request_name == 'Delete user':
            self.assert_status_code(MainPageLocators.RESPONSE_STATUS, self.users_api.delete_user(user_id).status)

    @BasePage.create_screenshot
    def should_be_status_code_and_body_equal_api_register_user(self, request_name: str, email: str, password: str) -> NoReturn:
        if request_name == 'Register successful':
            self.assert_status_code(MainPageLocators.RESPONSE_STATUS, self.users_api.register_user(email, password).status)
            self.assert_response_body(MainPageLocators.RESPONSE_BODY, self.users_api.register_user(email, password).response)
        elif request_name == 'Register unsuccessful':
            self.assert_status_code(MainPageLocators.RESPONSE_STATUS, self.users_api.register_user(email, password).status)
            self.assert_response_body(MainPageLocators.RESPONSE_BODY, self.users_api.register_user(email, password).response)

    @BasePage.create_screenshot
    def should_be_status_code_and_body_equal_api_login_user(self, request_name: str, email: str, password: str) -> NoReturn:
        if request_name == 'Login successful':
            self.assert_status_code(MainPageLocators.RESPONSE_STATUS, self.users_api.login_user(email, password).status)
            self.assert_response_body(MainPageLocators.RESPONSE_BODY, self.users_api.login_user(email, password).response)
        elif request_name == 'Login unsuccessful':
            self.assert_status_code(MainPageLocators.RESPONSE_STATUS, self.users_api.login_user(email, password).status)
            self.assert_response_body(MainPageLocators.RESPONSE_BODY, self.users_api.login_user(email, password).response)

    @BasePage.create_screenshot
    def should_be_status_code_and_body_equal_api_delayed_response(self, delay: int) -> NoReturn:
        self.assert_status_code(MainPageLocators.RESPONSE_STATUS, self.users_api.delayed_response(delay).status)
        self.assert_response_body(MainPageLocators.RESPONSE_BODY, self.users_api.delayed_response(delay).response)
