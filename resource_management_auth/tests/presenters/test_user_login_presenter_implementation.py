import pytest
from resource_management_auth.presenters.presenter_implementation \
    import PresenterImplementation
from resource_management_auth.storages.storage_implementation \
    import StorageImplementation
from unittest.mock import create_autospec, patch
from resource_management_auth.interactors.\
    user_login_interactor import UserLoginInteractor
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from common.dtos import UserAuthTokensDTO
user_auth_dto= UserAuthTokensDTO(
    user_id=1,
    access_token="ghkddddddddd",
    refresh_token="fdhhhhhhh",
    expires_in="2025,12,5"
)
class TestPresenterImplementation:

    @pytest.mark.django_db
    def test_user_login_raises_exception_for_invalid_user_name(self, snapshot, create_user):
        # Arrange

        user_name = "kavya"
        password = "iBHubs@021"
        storage = StorageImplementation()
        presenter = PresenterImplementation()
        oauth_storage = create_autospec(OAuth2SQLStorage)
        interactor = UserLoginInteractor(
            storage=storage,
            oauth_storage=oauth_storage)
        # Act

        result = interactor.user_login_wrapper(
            user_name=user_name,
            password=password,
            presenter=presenter
        )
        #  Assert
        print("**********************", result)
        print(result)
        snapshot.assert_match(result, "invalid_username")

    @pytest.mark.django_db
    def test_user_login_raises_exception_for_invalid_password(self,
                                                              snapshot,
                                                              create_user):
        # Arrange

        user_name = "divya"
        password = "jhjhjl"
        storage = StorageImplementation()
        presenter = PresenterImplementation()
        oauth_storage = create_autospec(OAuth2SQLStorage)
        interactor = UserLoginInteractor(
            storage=storage,
            oauth_storage=oauth_storage
        )

        # Act

        result = interactor.user_login_wrapper(
            user_name=user_name,
            password=password,
            presenter=presenter
        )
        #  Assert
        print("**********************", result)
        print(result)
        snapshot.assert_match(result, "invalid_password")

    @pytest.mark.django_db
    @patch.object(OAuthUserAuthTokensService, "create_user_auth_tokens",
                  return_value=user_auth_dto)
    def test_user_login_returns_user_access_token_dict(self,
                                                       snapshot,
                                                       create_user):
        # Arrange

        user_name = "divya"
        password = "ibhubs@123"
        storage = StorageImplementation()
        presenter = PresenterImplementation()
        expected_output = {
            'user_id': 1,
            'access_token': 'ghkddddddddd',
            'refresh_token': 'fdhhhhhhh',
            'expires_in': '2025,12,5',
            "is_admin": False
        }
        oauth_storage = create_autospec(OAuth2SQLStorage)
        service = create_autospec(OAuthUserAuthTokensService(oauth2_storage=oauth_storage))
        service.create_user_auth_tokens.return_value = user_auth_dto
        interactor = UserLoginInteractor(
            storage=storage,
            oauth_storage=oauth_storage
        )
        # Act

        result = interactor.user_login_wrapper(
            user_name=user_name,
            password=password,
            presenter=presenter
        )
        #  Assert
        print("**********************", result)
        print(result)
        assert result == expected_output
        #snapshot.assert_match(result, "accesstokendetails")
