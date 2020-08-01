from unittest.mock import create_autospec

import pytest

from resource_management.exceptions.exceptions import DuplicateResourceName
from resource_management.interactors.create_resource_interactor \
    import CreateResourceInteractor
from resource_management.interactors.storages.storage_interface \
    import StorageInterface
from resource_management.presenters.presenter_implementation \
    import PresenterImplementation


class TestCreateResourcePresenterImplementation:

    @pytest.mark.django_db
    def test_given_duplicate_resource_name_raises_exception(self,
                                                            create_resource,
                                                            snapshot,
                                                            resource_details_dto):

        # Arrange

        storage = create_autospec(StorageInterface)
        presenter = PresenterImplementation()
        interactor = CreateResourceInteractor(storage=storage)
        storage.validate_duplicate_resource_name.side_effect = DuplicateResourceName
        # Act
        response = interactor.create_resource_wrapper(
                resource_details_dto=resource_details_dto,
                presenter=presenter
            )
        # Assert
        snapshot.assert_match(response, "duplicate resource name")