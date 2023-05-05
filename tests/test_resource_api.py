import pytest
import allure
from utils.fakers import random_number


@allure.feature('Work with resource API')
class TestResourceAPI:

    @allure.title('Получение списка ресурсов')
    def test_get_list_resource_with_api(self, resource_api):

        with allure.step("Отправка GET-запроса для получения списка ресурсов"):
            list_source = resource_api.list_resource()

        with allure.step("Проверка, что в ответ на запрос приходит верный статус-код и тело ответа"):
            resource_api.should_be_valid_response_status_and_body_from_request_list_resource(list_source)

    @allure.title('Получение ресурса с id {resource_id}')
    @pytest.mark.parametrize('resource_id', [random_number(1, 12), random_number(13, 100)])
    def test_get_single_resource_with_api(self, resource_api, resource_id):

        with allure.step(f"Отправка GET-запроса для получения ресурса с id {resource_id}"):
            single_resource = resource_api.single_resource(resource_id)

        with allure.step("Проверка, что в ответ на запрос приходит верный статус-код и тело ответа"):
            resource_api.should_be_valid_response_status_and_body_from_request_single_resource(single_resource, resource_id)
