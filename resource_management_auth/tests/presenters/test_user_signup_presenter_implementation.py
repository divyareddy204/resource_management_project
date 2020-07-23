import pytest
from resource_management_auth.presenters.presenter_implementation \
    import PresenterImplementation
from resource_management_auth.storages.storage_implementation \
    import StorageImplementation
from resource_management_auth.interactors.\
    user_signup_interactor import UserSignUpInteractor



@pytest.mark.django_db
class TestPresenterImplementation:

    def test_user_sign_up_raises_exception_for_invalid_user_name(self, snapshot):
        # Arrange

        user_name = ""
        password = "iBHubs@021"
        storage = StorageImplementation()
        presenter = PresenterImplementation()
        interactor = UserSignUpInteractor(
            storage=storage)
        # Act

        result = interactor.user_signup_wrapper(
            user_name=user_name,
            password=password,
            presenter=presenter
        )
        #  Assert
        print("**********************", result)
        print(result)
        snapshot.assert_match(result, "invalid_username")


    def test_user_sign_up_raises_exception_for_invalid_password(self, snapshot):
        # Arrange

        user_name = "ibhubs"
        password = ""
        storage = StorageImplementation()
        presenter = PresenterImplementation()
        interactor = UserSignUpInteractor(
            storage=storage)
        # Act

        result = interactor.user_signup_wrapper(
            user_name=user_name,
            password=password,
            presenter=presenter
        )
        #  Assert
        print("**********************", result)
        print(result)
        snapshot.assert_match(result, "invalid_password")
