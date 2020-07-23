from typing import List
from resource_management_auth.interactors.presenters.presenter_interface import PresenterInterface
from django.http import response
from resource_management_auth.interactors.storages.dtos import UserAuthTokensDTO

class PresenterImplementation(PresenterInterface):

    def user_login_response(self, user_access_token_dto: UserAuthTokensDTO):
        print(user_access_token_dto)
        user_details = {
            "user_id": user_access_token_dto.user_id,
            "access_token": user_access_token_dto.access_token,
            "refresh_token": user_access_token_dto.refresh_token,
            "expires_in": str(user_access_token_dto.expires_in),
            "is_admin": user_access_token_dto.is_admin
        }
        #response_object = response.HttpResponse(user_details, 200)
        return user_details

    def raise_exception_for_invalid_user_name(self) -> response.HttpResponse:

        from resource_management_auth.constants.exception_messages import \
            INVALID_USER_NAME
        import json
        data ={
            "response": INVALID_USER_NAME[0],
            "http_status_code": 400,
            "res_status": INVALID_USER_NAME[1]
        }
        #response_object = response.HttpResponse(data, 400)
        return data

    def raise_exception_for_invalid_password(self) -> response.HttpResponse:
        from resource_management_auth.constants.exception_messages import \
            INVALID_PASSWORD
        import json
        data = {
            "response": INVALID_PASSWORD[0],
            "http_status_code": 400,
            "res_status": INVALID_PASSWORD[1]
        }
        #response_object = response.HttpResponse(data, 400)
        return data
