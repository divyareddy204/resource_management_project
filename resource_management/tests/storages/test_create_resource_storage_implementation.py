import pytest

from resource_management.exceptions.exceptions import DuplicateResourceName
from resource_management.interactors.create_resource_interactor import CreateResourceInteractor
from resource_management.models.resource import Resource
from resource_management.presenters.presenter_implementation import PresenterImplementation
from resource_management.storages.storage_implementation import StorageImplementation
from resource_management.interactors.storages.dtos import ResourceDetailsDTO
resource_details_dto = ResourceDetailsDTO(
    resource_name="resource1",
    description="resource is so and so...",
    resource_pic_url="image.png",
    resource_service="resource service is so and so...",
    resource_link="www.sample.com",
)

class TestCreateResourceStorageImplementation:

    @pytest.mark.django_db
    def test_given_duplicate_resource_name_raises_exception(self, create_resource):

        # Arrange

        storage = StorageImplementation()
        interactor = CreateResourceInteractor(storage=storage)

        # Act
        with pytest.raises(DuplicateResourceName):
            interactor.create_resource_interactor(
                resource_details_dto=resource_details_dto
            )
        # Assert

    @pytest.mark.django_db
    def test_create_resource_given_valid_details(self, create_resource):
        # Arrange
        resource_details_dto = ResourceDetailsDTO(
            resource_name="resource2",
            description="resource is so and so...",
            resource_pic_url="image.png",
            resource_service="resource service is so and so...",
            resource_link="www.sample2.com",
        )
        storage = StorageImplementation()
        interactor = CreateResourceInteractor(
            storage=storage)

        # Act
        interactor.create_resource_interactor(
            resource_details_dto=resource_details_dto)

        # Assert
        resource = Resource.objects.get(
            resource_name=resource_details_dto.resource_name)
        print(resource)
        assert resource.resource_link == resource_details_dto.resource_link
