from resource_management_auth.interactors.storages.storage_interface \
    import StorageInterface
from resource_management_auth.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management_auth.exceptions.exceptions import InvalidPassword, \
    InvalidUserName
from resource_management_auth.interactors.storages.dtos import UserAuthTokensDTO
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService


class UserLoginInteractor:

    def __init__(self, storage: StorageInterface,
                 oauth_storage: OAuth2SQLStorage()):
        self.storage = storage
        self.oauth_storage = oauth_storage

    def user_login_wrapper(self,
                           user_name: str, password: str,
                           presenter: PresenterInterface):

        try:
            user_auth_dto = self.user_login_interactor(
                user_name=user_name,
                password=password)
            return presenter.user_login_response(user_auth_dto)
        except InvalidUserName:
            print("username :*****************")
            return presenter.raise_exception_for_invalid_user_name()

        except InvalidPassword:
            print("password :*****************")
            return presenter.raise_exception_for_invalid_password()

    def user_login_interactor(self, user_name: str, password: str):

        self.storage.validate_user_name(user_name=user_name)
        k = self.storage.validate_password_for_user(
            user_name=user_name,
            password=password
        )
        user_details_dto = self.storage.get_user_details_of_given_user(
            user_name=user_name,
            password=password
        )

        service = OAuthUserAuthTokensService(oauth2_storage=self.oauth_storage)
        user_access_dto = service.create_user_auth_tokens(user_id=user_details_dto.user_id)
        user_auth_details = self._add_is_admin_to_user_access_dto(user_details_dto, user_access_dto)
        return user_auth_details

    def _add_is_admin_to_user_access_dto(self, user_details_dto, user_access_dto):
        print("**********mom***********", user_access_dto)
        return UserAuthTokensDTO(
            is_admin=user_details_dto.is_admin,
            user_id=user_details_dto.user_id,
            refresh_token=user_access_dto.refresh_token,
            expires_in=user_access_dto.expires_in,
            access_token=user_access_dto.access_token,
        )