import pytest
from resource_management.interactors.delete_resource_interactor \
    import DeleteResourceInteractor
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from resource_management.exceptions.exceptions import InvalidResourceIds
from resource_management.presenters.presenter_implementation import PresenterImplementation


class TestDeleteResourceInteractor:

    @pytest.fixture
    def storage_mock(self):
        from resource_management.interactors.storages.storage_interface \
            import StorageInterface
        from mock import create_autospec
        storage = create_autospec(StorageInterface)
        return storage

    def test_given_invalid_resource_ids_raises_exception(self,
                                                         storage_mock,
                                                         snapshot):

        # Arrange
        resource_ids = [1, 3]
        invalid_resource_ids = [3]
        presenter = PresenterImplementation()
        storage_mock.validate_resource_ids.side_effect = InvalidResourceIds(invalid_resource_ids)
        interactor = DeleteResourceInteractor(storage=storage_mock)

        # Act
        response =  interactor.delete_resource_wrapper(
                resource_ids=resource_ids,
                presenter=presenter
            )

        # Assert
        storage_mock.validate_resource_ids.assert_called_once_with(
            resource_ids=resource_ids
        )
        snapshot.assert_match(response, "invalid resource ids")


    def test_given_duplicate_resource_ids_raises_exception(self,
                                                           storage_mock,
                                                           snapshot):

        # Arrange
        resource_ids = [1, 3, 1]
        duplicate_resource_ids = [1, 1]
        presenter = PresenterImplementation()
        interactor = DeleteResourceInteractor(storage=storage_mock)

        # Act
        response = interactor.delete_resource_wrapper(
                resource_ids=resource_ids,
                presenter=presenter
            )

        # Assert
        snapshot.assert_match(response, "duplicate resource ids")
