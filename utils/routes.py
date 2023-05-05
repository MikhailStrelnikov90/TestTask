from enum import Enum


class APIRoutes(str, Enum):
    LIST_USERS = 'api/users?page='
    SINGLE_USER = 'api/users/'
    LIST_RESOURCE = 'api/unknown'
    SINGLE_RESOURCE = 'api/unknown/'
    CREATE_USER = 'api/users'
    EDIT_USER = 'api/users/'
    REGISTER = 'api/register'
    LOGIN = 'api/login'
    DELAYED = 'api/users?delay='

    def __str__(self) -> str:
        return self.value
