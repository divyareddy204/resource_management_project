from resource_management_auth.storages.storage_implementation import StorageImplementation
from resource_management_auth.presenters.presenter_implementation import PresenterImplementation
from unittest.mock import create_autospec
from resource_management_auth.interactors.\
    user_login_interactor import UserLoginInteractor
from common.oauth2_storage import OAuth2SQLStorage
import pytest

user_details_dto = {

}

@pytest.mark.django_db
def test_user_login_given_valid_user_name_password(create_user):

    # Arrange
    user_name = "divya"
    password = "ibhubs@123"
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    oauth_storage = create_autospec(OAuth2SQLStorage)
    interactor = UserLoginInteractor(
        storage=storage,
        oauth_storage=oauth_storage
    )
    # Act

    user_details_dto = storage.get_user_details_of_given_user(
        user_name=user_name,
        password=password
    )

    # Assert
    print(user_details_dto)
