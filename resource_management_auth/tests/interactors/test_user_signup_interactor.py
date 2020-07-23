import pytest
from unittest.mock import patch
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management_auth.interactors.\
    user_signup_interactor import UserSignUpInteractor

from resource_management_auth.exceptions.exceptions \
    import InvalidUserName, InvalidPassword


class TestUserSignUpInteractor:

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

    @patch("resource_management_auth.interactors.user_signup_interactor.UserSignUpInteractor.validate_user_name")
    def test_given_invalid_user_name_raises_invalid_user_name_exception(self,
                                                                        validate_user_name,
                                                                        storage_mock,
                                                                        presenter_mock):

            # Arrange

            user_name = ""
            password = "23455634"
            interactor = UserSignUpInteractor(
                storage=storage_mock)
            validate_user_name.side_effect = InvalidUserName
            presenter_mock.raise_exception_for_invalid_user_name.side_effect = BadRequest

            # Act

            with pytest.raises(BadRequest):
                interactor.user_signup_wrapper(
                    user_name=user_name,
                    password=password,
                    presenter=presenter_mock
                )
            # Assert
            validate_user_name.assert_called_once()
            presenter_mock.raise_exception_for_invalid_user_name.assert_called_once()

    @patch("resource_management_auth.interactors.user_signup_interactor.UserSignUpInteractor.validate_password")
    def test_given_invalid_password_raises_invalid_user_name_exception(self,
                                                                        validate_password,
                                                                        storage_mock,
                                                                        presenter_mock):

            # Arrange

            user_name = "ibhubs"
            password = ""
            interactor = UserSignUpInteractor(
                storage=storage_mock)
            validate_password.side_effect = InvalidPassword
            presenter_mock.raise_exception_for_invalid_password.side_effect = BadRequest
            # Act
            with pytest.raises(BadRequest):
                interactor.user_signup_wrapper(
                    user_name=user_name,
                    password=password,
                    presenter=presenter_mock
                )
            #  Assert
            validate_password.assert_called_once()
            presenter_mock.raise_exception_for_invalid_password.assert_called_once()

    def test_user_signup_given_valid_details(self,
                                             storage_mock,
                                             presenter_mock):
        # Arrange

        user_name = "ibhubs"
        password = "iBHubs@021"
        interactor = UserSignUpInteractor(
            storage=storage_mock)
        #storage_mock.create_user(user_name=user_name, password=password)
        # Act

        interactor.user_signup_wrapper(
            user_name=user_name,
            password=password,
            presenter=presenter_mock
        )
        #  Assert
        storage_mock.create_user.assert_called_once_with(
            user_name=user_name, password=password)
