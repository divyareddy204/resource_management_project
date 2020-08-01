from resource_management.interactors.get_resource_details_interactor \
    import GetResourceDetailsInteractor
from resource_management.interactors.storages.dtos import CompleteResourceDetailsDTO
from resource_management.interactors.storages.storage_interface \
    import StorageInterface
from resource_management.presenters.presenter_implementation import PresenterImplementation


class TestGetResourceDetails:

    def test_get_resource_details_empty(self,
                                        snapshot):

        # Arrange
        from mock import create_autospec
        presenter = PresenterImplementation()
        storage = create_autospec(StorageInterface)
        storage.get_all_resources_details.return_value = []
        interactor = GetResourceDetailsInteractor(storage=storage)
        # Act
        resource_details_list = interactor.get_resource_details_wrapper(presenter=presenter)

        # Assert
        assert resource_details_list == []
        storage.get_all_resources_details.assert_called_once_with()

    def test_get_resource_details(self,
                                  snapshot,
                                  resource_details_dtos,
                                  get_resource_details_response):

        #Arrange
        expected_output = get_resource_details_response
        from mock import create_autospec
        presenter = PresenterImplementation()
        storage = create_autospec(StorageInterface)
        interactor = GetResourceDetailsInteractor(storage=storage)
        storage.get_all_resources_details.return_value = resource_details_dtos

        # Act
        resource_details_list = interactor.get_resource_details_wrapper(presenter=presenter)

        # Assert
        assert resource_details_list == expected_output
        storage.get_all_resources_details.assert_called_once_with()
