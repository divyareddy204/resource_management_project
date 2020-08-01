import pytest

from resource_management.exceptions.exceptions import \
    InvalidResourceIds, DuplicateResourceIds
from resource_management.interactors.delete_resource_interactor import DeleteResourceInteractor
from resource_management.models.resource import Resource
from resource_management.storages.storage_implementation import StorageImplementation

class TestDeleteResourceStorageImplementation:

    @pytest.mark.django_db
    def test_given_invalid_resource_ids_raises_exception(self, create_resource):

        # Arrange
        resource_ids = [3, 1]
        invalid_resource_ids = [3]
        storage = StorageImplementation()
        interactor = DeleteResourceInteractor(storage=storage)

        # Act
        with pytest.raises(InvalidResourceIds):
            interactor.delete_resource_interactor(
                resource_ids=resource_ids
            )
        # Assert

    @pytest.mark.django_db
    def test_delete_resource_given_valid_details(self, create_resource):
        # Arrange
        resource_ids = [1]
        storage = StorageImplementation()
        interactor = DeleteResourceInteractor(
            storage=storage)

        # Act
        interactor.delete_resource_interactor(
            resource_ids=resource_ids)

        # Assert