import allure
import pytest


@allure.feature('Work with Main page (UI)')
class TestMainPage:

    @pytest.mark.parametrize('request_name, user_id', [('list_users', 2), ('single_user', 2), ('single_user_not_found', 23)])
    @allure.title('Get {request_name}')
    def test_get_user(self, main_page, browser, api_reqres, request_name: str, user_id: int):

        with allure.step("Открытие браузера и страницы сайта"):
            main_page.open()

        with allure.step(f"Открытие информации о запросе {request_name}"):
            main_page.click_on_user(request_name)

        with allure.step(f"Проверка, что тело и статус-код ответа на запрос {request_name} совпадают с ответом, полученным с помощью вызова API"):
            main_page.should_be_status_code_and_body_equal_api_get_users(request_name, user_id)

    @pytest.mark.parametrize('request_name, resource_id', [('list_resource', None), ('single_resource', 2), ('single_resource_not_found', 23)])
    @allure.title('Get {request_name}')
    def test_get_resource(self, browser, main_page, api_reqres, request_name: str, resource_id: int):

        with allure.step("Открытие браузера и страницы сайта"):
            main_page.open()

        with allure.step(f"Открытие информации о запросе {request_name}"):
            main_page.click_on_resource(request_name)

        with allure.step(f"Проверка, что тело и статус-код ответа на запрос {request_name} совпадают с ответом, полученным с помощью вызова API"):
            main_page.should_be_status_code_and_body_equal_api_get_resource(request_name, resource_id)

    @pytest.mark.parametrize('request_name, name, job, user_id', [('Create user', "morpheus", "leader", None), ('Update (PUT) user', "morpheus", "zion resident", 2), ('Update (PATCH) user', "morpheus", "zion resident", 2), ('Delete user', None, None, 2)])
    @allure.title('{request_name}')
    def test_edit_user(self, browser, main_page, api_reqres, request_name: str, name: str, job: str, user_id: int):

        with allure.step("Открытие браузера и страницы сайта"):
            main_page.open()

        with allure.step(f"Открытие информации о запросе {request_name}"):
            main_page.click_on_edit_user(request_name)

        with allure.step(f"Проверка, что тело и статус-код ответа на запрос {request_name} совпадают с ответом, полученным с помощью вызова API"):
            main_page.should_be_status_code_and_body_equal_api_edit_user(request_name, name, job, user_id)

    @pytest.mark.parametrize('request_name, email, password', [('Register successful', "eve.holt@reqres.in", "pistol"), ('Register unsuccessful', "sydney@fife", None)])
    @allure.title('{request_name}')
    def test_register(self, browser, main_page, api_reqres, request_name: str, email: str, password: str):

        with allure.step("Открытие браузера и страницы сайта"):
            main_page.open()

        with allure.step(f"Открытие информации о запросе {request_name}"):
            main_page.click_on_register_user(request_name)

        with allure.step(f"Проверка, что тело и статус-код ответа на запрос {request_name} совпадают с ответом, полученным с помощью вызова API"):
            main_page.should_be_status_code_and_body_equal_api_register_user(request_name, email, password)

    @pytest.mark.parametrize('request_name, email, password', [('Login successful', "eve.holt@reqres.in", "cityslicka"), ('Login unsuccessful', "peter@klaven", None)])
    @allure.title('{request_name}')
    def test_login(self, browser, main_page, api_reqres, request_name: str, email: str, password: str):

        with allure.step("Открытие браузера и страницы сайта"):
            main_page.open()

        with allure.step(f"Открытие информации о запросе {request_name}"):
            main_page.click_on_login_user(request_name)

        with allure.step(f"Проверка, что тело и статус-код ответа на запрос {request_name} совпадают с ответом, полученным с помощью вызова API"):
            main_page.should_be_status_code_and_body_equal_api_login_user(request_name, email, password)

    @pytest.mark.parametrize('delay', [3])
    @allure.title('Delayed response')
    def test_delayed(self, browser, main_page, api_reqres, delay: int):

        with allure.step("Открытие браузера и страницы сайта"):
            main_page.open()

        with allure.step("Открытие информации о запросе Delayed response"):
            main_page.click_on_delayed_response()

        with allure.step("Проверка, что тело ответа и статус-код запроса Delayed response совпадает с ответом, полученным с помощью вызова API"):
            main_page.should_be_status_code_and_body_equal_api_delayed_response(delay)
