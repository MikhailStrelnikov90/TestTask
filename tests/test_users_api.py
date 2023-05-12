import pytest
import allure
from utils.fakers import random_number, random_string, random_email


@allure.feature('Work with users API')
class TestUsersAPI:
    
    @allure.title('Получение списка пользователей со страницы {page}')
    @pytest.mark.parametrize('page', [random_number(1, 2), random_number(3, 100)])
    def test_get_list_users(self, users_api, page: int):

        with allure.step(f"Отправка GET-запроса на получение списка пользователей со страницы {page}"):
            list_users = users_api.list_users(page)

        with allure.step("Проверка, что в ответ на запрос приходит верный статус-код и тело ответа"):
            users_api.should_be_valid_response_status_and_body_from_request_list_users(list_users)

    @allure.title('Получение данных пользователя с id {user_id}')
    @pytest.mark.parametrize('user_id', [random_number(1, 12), random_number(13, 100)])
    def test_get_single_user_with_api(self, users_api, user_id: int):

        with allure.step(f"Отправка GET-запроса на получение данных пользователя c id {user_id}"):
            single_user = users_api.single_users(user_id)

        with allure.step("Проверка, что в ответ на запрос приходит верный статус-код и тело ответа"):
            users_api.should_be_valid_response_status_and_body_from_request_single_users(single_user, user_id)

    @allure.title('Создание пользователя {name}')
    @pytest.mark.parametrize('name, job', [(random_string(6, 10), random_string(6, 10)), (random_string(6, 10), None), (None, random_string(6, 10)), (None, None)])
    def test_create_user_with_api(self, users_api, name: str, job: str):
        
        with allure.step("Отправка POST-запроса для создания пользователя"):
            create_user = users_api.create_user(name, job)

        with allure.step("Проверка, что в ответ на запрос приходит верный статус-код и тело ответа"):
            users_api.should_be_valid_response_status_and_body_from_request_create_user(create_user, name, job)

    @allure.title('Редактирование пользователя с id {user_id} с помощью метода {method}')
    @pytest.mark.parametrize('user_id, method, name, job', [(random_number(1, 10), "PUT", random_string(6, 10), random_string(10, 15)), (random_number(1, 10), "PATCH", random_string(6, 10), random_string(10, 15))])
    def test_update_user_with_api(self, users_api, user_id: int, method: str, name: str, job: str):

        with allure.step(f"Отправка {method}-запроса для редактирования пользователя"):
            update_user = users_api.update_user(method, user_id, name, job)

        with allure.step("Проверка, что в ответ на запрос приходит верный статус-код и тело ответа"):
            users_api.should_be_valid_response_status_and_body_from_request_update_user(update_user)

    @allure.title('Удаление пользователя с id {user_id}')
    @pytest.mark.parametrize('user_id', [random_number(1, 10)])
    def test_delete_user_with_api(self, users_api, user_id: int):

        with allure.step(f"Отправка DELETE-запроса для удаления пользователя с id {user_id}"):
            delete_user = users_api.delete_user(user_id)

        with allure.step("Проверка, что в ответ на запрос приходит верный статус-код и тело ответа"):
            users_api.should_be_valid_response_status_and_body_from_request_delete_user(delete_user)

    @allure.title('Регистрация пользователя с email {email} и паролем {password}')
    @pytest.mark.parametrize('email, password', [("eve.holt@reqres.in", random_string(8, 10)), (random_email(), None), (None, random_string(8, 10)), (None, None)])
    def test_register_user_with_api(self, users_api, email: str | None, password: str | None):

        with allure.step("Отправка POST-запроса для регистрации пользователя"):
            register_user = users_api.register_user(email, password)

        with allure.step("Проверка, что в ответ на запрос приходит верный статус-код и тело ответа"):
            users_api.should_be_valid_response_status_and_body_from_request_register_user(register_user, email, password)

    @allure.title('Авторизация пользователя с email {email} и паролем {password}')
    @pytest.mark.parametrize('email, password', [("eve.holt@reqres.in", random_string(8, 10)), (random_email(), None), (None, random_string(8, 10)), (None, None)])
    def test_login_user_with_api(self, users_api, email: str | None, password: str | None):

        with allure.step("Отправка POST-запроса для авторизации пользователя"):
            login_user = users_api.login_user(email, password)

        with allure.step("Проверка, что в ответ на запрос приходит верный статус-код и тело ответа"):
            users_api.should_be_valid_response_status_and_body_from_request_login_user(login_user, email, password)

    @pytest.mark.parametrize('delay', [random_number(5, 10)])
    @allure.title('Получение списка пользователей с задержкой {delay}')
    def test_delayed_response_with_api(self, users_api, delay: int):

        with allure.step(f"Отправка GET-запроса для получения списка пользователей с задержкой {delay}"):
            get_list_users_with_delay = users_api.delayed_response(delay)

        with allure.step("Проверка, что в ответ на запрос приходит верный статус-код и тело ответа"):
            users_api.should_be_valid_response_status_and_body_from_request_list_users(get_list_users_with_delay)
