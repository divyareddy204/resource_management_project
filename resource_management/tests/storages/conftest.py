import pytest

from resource_management.models.resource import Resource

@pytest.fixture
def create_resource():

    from resource_management.interactors.storages.dtos import ResourceDetailsDTO
    resource_dto = ResourceDetailsDTO(
        resource_name="resource1",
        description="resource is so and so...",
        resource_pic_url="image.png",
        resource_service="resource service is so and so...",
        resource_link="www.sample.com",
    )
    Resource.objects.create(
        resource_name=resource_dto.resource_name,
        description=resource_dto.description,
        resource_pic_url=resource_dto.resource_pic_url,
        resource_service=resource_dto.resource_service,
        resource_link=resource_dto.resource_link
    )