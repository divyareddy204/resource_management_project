import pytest
from resource_management.interactors.create_resource_interactor \
    import CreateResourceInteractor
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management.exceptions.exceptions import DuplicateResourceName


class TestCreateResourceInteractor:

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

    def test_given_duplicate_resource_name_raises_exception(self,
                                                            storage_mock,
                                                            presenter_mock,
                                                            resource_details_dto):

        # Arrange
        storage_mock.validate_duplicate_resource_name.side_effect = DuplicateResourceName
        presenter_mock.raise_exception_for_duplicate_resource_name.side_effect = BadRequest
        interactor = CreateResourceInteractor(storage=storage_mock)

        # Act
        with pytest.raises(BadRequest):
            interactor.create_resource_wrapper(
                resource_details_dto=resource_details_dto,
                presenter=presenter_mock
            )

        # Assert
        storage_mock.validate_duplicate_resource_name.assert_called_once_with(
            resource_name=resource_details_dto.resource_name
        )
        presenter_mock.raise_exception_for_duplicate_resource_name.assert_called_once_with()

    def test_create_resource_given_valid_details(self,
                                                 storage_mock,
                                                 presenter_mock,
                                                 resource_details_dto):

        # Arrange
        interactor = CreateResourceInteractor(
            storage=storage_mock)

        # Act
        interactor.create_resource_wrapper(
            resource_details_dto=resource_details_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.create_resource.assert_called_once_with(
            resource_details_dto=resource_details_dto
        )


