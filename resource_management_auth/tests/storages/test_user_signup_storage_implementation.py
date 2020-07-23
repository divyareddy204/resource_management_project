import pytest
from resource_management_auth.storages.storage_implementation import StorageImplementation
from resource_management_auth.presenters.presenter_implementation import PresenterImplementation
from resource_management_auth.models import User
from resource_management_auth.interactors.\
    user_signup_interactor import UserSignUpInteractor

class TestUserSignupStorageImplimentation:

    @pytest.mark.django_db
    def test_user_signup_given_valid_details(self):
        # Arrange

        storage = StorageImplementation()
        presenter = PresenterImplementation
        user_name = "divya"
        password = "iBHubs@021"
        interactor = UserSignUpInteractor(
            storage=storage)

        interactor.user_signup_wrapper(
            user_name=user_name,
            password=password,
            presenter=presenter
        )
        #  Assert
        user = User.objects.get(username=user_name)
        assert user.username == user_name
        assert user.check_password(password)