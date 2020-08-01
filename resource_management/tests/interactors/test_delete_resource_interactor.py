import pytest
from resource_management.interactors.delete_resource_interactor \
    import DeleteResourceInteractor
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from resource_management.exceptions.exceptions import InvalidResourceIds

class TestDeleteResourceInteractor:

    @pytest.fixture
    def storage_mock(self):
        from resource_management.interactors.storages.storage_interface \
            import StorageInterface
        from mock import create_autospec
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from resource_management.interactors.presenters.presenter_interface \
            import PresenterInterface
        from mock import create_autospec
        presenter = create_autospec(PresenterInterface)
        return presenter

    def test_given_invalid_resource_ids_raises_exception(self,
                                                            storage_mock,
                                                            presenter_mock):

        # Arrange
        resource_ids = [1, 3]
        invalid_resource_ids = [3]
        storage_mock.validate_resource_ids.side_effect = InvalidResourceIds(invalid_resource_ids)
        presenter_mock.raise_exception_for_invalid_resource_ids.side_effect = NotFound
        interactor = DeleteResourceInteractor(storage=storage_mock)

        # Act
        with pytest.raises(NotFound):
            interactor.delete_resource_wrapper(
                resource_ids=resource_ids,
                presenter=presenter_mock
            )

        # Assert
        storage_mock.validate_resource_ids.assert_called_once_with(
            resource_ids=resource_ids
        )
        presenter_mock.raise_exception_for_invalid_resource_ids.assert_called_once()
        call_obj = presenter_mock. \
            raise_exception_for_invalid_resource_ids.call_args
        error_obj = call_obj.args[0]
        assert error_obj.invalid_resource_ids == invalid_resource_ids


    def test_given_duplicate_resource_ids_raises_exception(self,
                                                            storage_mock,
                                                            presenter_mock):

        # Arrange
        resource_ids = [1, 3, 1]
        duplicate_resource_ids = [1, 1]
        presenter_mock.raise_exception_for_duplicate_resource_ids.side_effect = BadRequest
        interactor = DeleteResourceInteractor(storage=storage_mock)

        # Act
        with pytest.raises(BadRequest):
            interactor.delete_resource_wrapper(
                resource_ids=resource_ids,
                presenter=presenter_mock
            )

        # Assert
        presenter_mock.raise_exception_for_duplicate_resource_ids.assert_called_once()
        call_obj = presenter_mock. \
            raise_exception_for_duplicate_resource_ids.call_args
        error_obj = call_obj.args[0]
        assert error_obj.duplicate_resource_ids == duplicate_resource_ids

    def test_delete_resource_given_valid_details(self, storage_mock, presenter_mock):

        # Arrange
        resource_ids = [2, 4, 5]
        interactor = DeleteResourceInteractor(
            storage=storage_mock)

        # Act
        interactor.delete_resource_wrapper(
            resource_ids=resource_ids,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.delete_resource.assert_called_once_with(
            resource_ids=resource_ids,
        )
