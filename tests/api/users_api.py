import json
from typing import NoReturn
from jsonschema import validate
from utils.models.response_model import ResponseModel
from utils.routes import APIRoutes
from utils.models.users_model import (DefaultRegister, DefaultLogin, DefaultUpdateUser,
                                      DefaultListUsers, DefaultSingleUser, DefaultCreateUser,
                                      DefaultCreateUserWithoutJob, DefaultCreateUserWithoutData, DefaultCreateUserWithoutName)


class UsersAPI:

    def __init__(self, api_reqres) -> None:
        self.api_reqres = api_reqres

    def list_users(self, page: int) -> ResponseModel:
        response = self.api_reqres.get_request(APIRoutes.LIST_USERS, params={'page': page})
        return ResponseModel(status=response.status_code, response=response.json())

    def single_users(self, user_id: int) -> ResponseModel:
        response = self.api_reqres.get_request(f"{APIRoutes.SINGLE_USER}{user_id}")
        return ResponseModel(status=response.status_code, response=response.json())

    def create_user(self, name: str, job: str) -> ResponseModel:
        response = self.api_reqres.post_request(APIRoutes.CREATE_USER, data=json.dumps({"name": name, "job": job}), headers={'Content-Type': 'application/json'})
        return ResponseModel(status=response.status_code, response=response.json())

    def update_user(self, method: str, user_id: int, name: str, job: str) -> ResponseModel:
        if method == "PUT":
            response = self.api_reqres.put_request(f"{APIRoutes.EDIT_USER}{user_id}", data=json.dumps({"name": name, "job": job}), headers={'Content-Type': 'application/json'})
        else:
            response = self.api_reqres.patch_request(f"{APIRoutes.EDIT_USER}{user_id}", data=json.dumps({"name": name, "job": job}), headers={'Content-Type': 'application/json'})
        return ResponseModel(status=response.status_code, response=response.json())

    def delete_user(self, user_id: int) -> ResponseModel:
        response = self.api_reqres.delete_request(f"{APIRoutes.EDIT_USER}{user_id}")
        return ResponseModel(status=response.status_code)

    def register_user(self, email: str | None, password: str | None) -> ResponseModel:
        if email is None and password is not None:
            payload = json.dumps({"password": password})
        elif email is not None and password is None:
            payload = json.dumps({"email": email})
        else:
            payload = json.dumps({"email": email, "password": password})
        response = self.api_reqres.post_request(APIRoutes.REGISTER, data=payload, headers={'Content-Type': 'application/json'})
        return ResponseModel(status=response.status_code, response=response.json())

    def login_user(self, email: str | None, password: str | None) -> ResponseModel:
        if email is None and password is not None:
            payload = json.dumps({"password": password})
        elif email is not None and password is None:
            payload = json.dumps({"email": email})
        else:
            payload = json.dumps({"email": email, "password": password})
        response = self.api_reqres.post_request(APIRoutes.LOGIN, data=payload, headers={'Content-Type': 'application/json'})
        return ResponseModel(status=response.status_code, response=response.json())

    def delayed_response(self, delay: int) -> ResponseModel:
        response = self.api_reqres.get_request(APIRoutes.DELAYED, params={'delay': delay})
        return ResponseModel(status=response.status_code, response=response.json())

    @staticmethod
    def should_be_valid_response_status_and_body_from_request_list_users(list_users) -> NoReturn:
        assert list_users.status == 200
        validate(list_users.response, DefaultListUsers.schema())

    @staticmethod
    def should_be_valid_response_status_and_body_from_request_single_users(single_user, user_id: int) -> NoReturn:
        if user_id <= 12:
            assert single_user.status == 200
            validate(single_user.response, DefaultSingleUser.schema())
        else:
            assert single_user.status == 404

    @staticmethod
    def should_be_valid_response_status_and_body_from_request_create_user(create_user, name: str | None, job: str | None) -> NoReturn:
        assert create_user.status == 201
        if name is None and job is None:
            validate(create_user.response, DefaultCreateUserWithoutData.schema())
        elif name is None and job is not None:
            validate(create_user.response, DefaultCreateUserWithoutName.schema())
        elif name is not None and job is None:
            validate(create_user.response, DefaultCreateUserWithoutJob.schema())
        else:
            validate(create_user.response, DefaultCreateUser.schema())

    @staticmethod
    def should_be_valid_response_status_and_body_from_request_update_user(update_user) -> NoReturn:
        assert update_user.status == 200
        validate(update_user.response, DefaultUpdateUser.schema())

    @staticmethod
    def should_be_valid_response_status_and_body_from_request_delete_user(delete_user) -> NoReturn:
        assert delete_user.status == 204

    @staticmethod
    def should_be_valid_response_status_and_body_from_request_register_user(register_user, email: str | None, password: str | None) -> NoReturn:
        if email is None or password is None:
            assert register_user.status == 400
            assert register_user.response["error"] == "Missing password" or register_user.response["error"] == "Missing email or username"
        else:
            assert register_user.status == 200
            validate(register_user.response, DefaultRegister.schema())

    @staticmethod
    def should_be_valid_response_status_and_body_from_request_login_user(login_user, email: str | None, password: str | None) -> NoReturn:
        if email is None or password is None:
            assert login_user.status == 400
            assert login_user.response["error"] == "Missing password" or login_user.response["error"] == "Missing email or username"
        else:
            assert login_user.status == 200
            validate(login_user.response, DefaultLogin.schema())
