from typing import NoReturn
from utils.models.response_model import ResponseModel
from utils.routes import APIRoutes
from jsonschema import validate
from utils.models.resource_model import (DefaultListResource, DefaultSingleResource)


class ResourceAPI:

    def __init__(self, api_reqres) -> None:
        self.api_reqres = api_reqres

    def list_resource(self) -> ResponseModel:
        response = self.api_reqres.get_request(APIRoutes.LIST_RESOURCE)
        return ResponseModel(status=response.status_code, response=response.json())

    def single_resource(self, resource_id: int) -> ResponseModel:
        response = self.api_reqres.get_request(f"{APIRoutes.SINGLE_RESOURCE}{resource_id}")
        return ResponseModel(status=response.status_code, response=response.json())

    @staticmethod
    def should_be_valid_response_status_and_body_from_request_list_resource(list_resource) -> NoReturn:
        assert list_resource.status == 200
        validate(list_resource.response, DefaultListResource.schema())

    @staticmethod
    def should_be_valid_response_status_and_body_from_request_single_resource(single_resource, resource_id: int) -> NoReturn:
        if resource_id <= 12:
            assert single_resource.status == 200
            validate(single_resource.response, DefaultSingleResource.schema())
        else:
            assert single_resource.status == 404
