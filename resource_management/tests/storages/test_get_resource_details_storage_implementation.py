import pytest

from resource_management.interactors.get_resource_details_interactor \
    import GetResourceDetailsInteractor
from resource_management.storages.storage_implementation \
    import StorageImplementation


class TestGetResourceDetails:

    @pytest.mark.django_db
    def test_get_resource_details(self,
                                  snapshot,
                                  create_resource):

        # Arrange
        storage = StorageImplementation()
        interactor = GetResourceDetailsInteractor(storage=storage)
        # Act
        resource_details_list = interactor.get_resource_details_interactor()

        # Assert
        snapshot.assert_match(resource_details_list, "resource_details_dtos")

    @pytest.mark.django_db
    def test_get_resource_details_empty(self,
                                        snapshot):
        # Arrange
        storage = StorageImplementation()
        interactor = GetResourceDetailsInteractor(storage=storage)
        # Act
        resource_details_list = interactor.get_resource_details_interactor()

        # Assert
        snapshot.assert_match(resource_details_list, "resource_details_dtos")

