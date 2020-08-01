import pytest
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import NotFound
from resource_management_auth.interactors.user_login_interactor import UserLoginInteractor
from resource_management_auth.exceptions.exceptions import InvalidUserName, InvalidPassword
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from common.dtos import UserAuthTokensDTO
user_auth_dto= UserAuthTokensDTO(
    user_id=1,
    access_token="ghkddddddddd",
    refresh_token="fdhhhhhhh",
    expires_in="2025,12,5"
)

class TestUserLoginInteractor:

    @pytest.fixture
    def storage_mock(self):
        from resource_management_auth.interactors.storages.storage_interface \
            import StorageInterface
        from mock import create_autospec
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from resource_management_auth.interactors.presenters.presenter_interface \
            import PresenterInterface
        from mock import create_autospec
        presenter = create_autospec(PresenterInterface)
        return presenter


    def test_user_login_given_invalid_user_name(self,
                                                storage_mock,
                                                presenter_mock):

        # Arrange
        user_name = "0932825493"
        password = "password"
        oauth_storage = create_autospec(OAuth2SQLStorage)
        interactor = UserLoginInteractor(
            storage=storage_mock,
            oauth_storage=oauth_storage
            )
        storage_mock.validate_user_name.side_effect = InvalidUserName
        presenter_mock.raise_exception_for_invalid_user_name.side_effect = NotFound
        # Act
        with pytest.raises(NotFound):
            interactor.user_login_wrapper(
                user_name=user_name,
                password=password,
                presenter=presenter_mock
                )

        # Assert
        storage_mock.validate_user_name.assert_called_once_with(
           user_name=user_name)
        presenter_mock.raise_exception_for_invalid_user_name.assert_called_once_with()


    def test_user_login_given_invalid_password(self,
                                               storage_mock,
                                               presenter_mock):

        # Arrange
        user_name = "0932825493"
        password = "password"
        oauth_storage = create_autospec(OAuth2SQLStorage)
        interactor = UserLoginInteractor(
            storage=storage_mock,
            oauth_storage=oauth_storage
            )
        storage_mock.validate_password_for_user.side_effect= InvalidPassword
        presenter_mock.raise_exception_for_invalid_password.side_effect = NotFound
        # Act
        with pytest.raises(NotFound):
            interactor.user_login_wrapper(
                user_name=user_name,
                password=password,
                presenter=presenter_mock
            )

        # Assert
        storage_mock.validate_password_for_user.assert_called_once_with(
            user_name=user_name, password=password)
        presenter_mock.raise_exception_for_invalid_password.assert_called_once_with()

    @patch.object(OAuthUserAuthTokensService, "create_user_auth_tokens",
                  return_value=user_auth_dto)
    def test_user_login_given_valid_user_name_password(self,
                                              storage_mock,
                                              presenter_mock):
        from resource_management_auth.interactors.storages.dtos import UserDetailsDTO

        # Arrange
        user_name = "IBITP"
        password = "password"
        user_id = 1
        user_details_dto = UserDetailsDTO (
            user_id = user_id,
            is_admin=True
        )
        expected_output = {
            'user_id': 1,
            'access_token': 'ghkddddddddd',
            'refresh_token': 'fdhhhhhhh',
            'expires_in': '2025, 12, 5'
        }
        oauth_storage = create_autospec(OAuth2SQLStorage)
        service = create_autospec(OAuthUserAuthTokensService(oauth2_storage=oauth_storage))
        interactor = UserLoginInteractor(
            storage=storage_mock,
            oauth_storage=oauth_storage
            )

        presenter_mock.user_login_response.return_value = {
            'user_id': 1,
            'access_token': 'ghkddddddddd',
            'refresh_token': 'fdhhhhhhh',
            'expires_in': '2025, 12, 5'}
        storage_mock.get_user_details_of_given_user.return_value = user_details_dto
        service.create_user_auth_tokens.return_value = user_auth_dto
        # Act
        response = interactor.user_login_wrapper(
            user_name=user_name,
            password=password,
            presenter=presenter_mock
            )

        # Assert
        service.create_user_auth_tokens.assert_called_once_with(user_id=user_id)
        assert response == expected_output
