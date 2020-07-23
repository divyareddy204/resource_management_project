from abc import ABC
from abc import abstractmethod
from resource_management_auth.interactors.storages.dtos import UserAuthTokensDTO
from django.http import response


class PresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_invalid_user_name(self) -> response.HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_password(self) -> response.HttpResponse:
        pass

    @abstractmethod
    def user_login_response(self, user_auth_dto: UserAuthTokensDTO) -> response.HttpResponse:
        pass
