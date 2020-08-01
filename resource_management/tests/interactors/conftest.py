import pytest

from resource_management.interactors.storages.dtos import ResourceDetailsDTO, CompleteResourceDetailsDTO
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

@pytest.fixture
def resource_details_dto():
    resource_details_dto = ResourceDetailsDTO(
        resource_name="resource1",
        description="resource is so and so...",
        resource_pic_url="image.png",
        resource_service="resource service is so and so...",
        resource_link="www.sample.com",
    )
    return resource_details_dto

@pytest.fixture
def resource_details_dtos():
    resource_details_dtos = [CompleteResourceDetailsDTO(
            resource_id=1,
            resource_name="resource1",
            description="resource is so and so...",
            resource_pic_url="image1.png",
            resource_service="resource service is so and so...",
            resource_link="www.sample1.com",
        ),
        CompleteResourceDetailsDTO(
            resource_id=2,
            resource_name="resource2",
            description="resource is so and so...",
            resource_pic_url="image2.png",
            resource_service="resource service is so and so...",
            resource_link="www.sample2.com",
        ),
    ]
    return resource_details_dtos

@pytest.fixture
def get_resource_details_response():
    expected_output = [
        {
            "resource_id": 1,
            "resource_name": "resource1",
            "description": "resource is so and so...",
            "resource_pic_url": "image1.png",
            "resource_service": "resource service is so and so...",
            "resource_link": "www.sample1.com",
        },
        {
            "resource_id": 2,
            "resource_name": "resource2",
            "description": "resource is so and so...",
            "resource_pic_url": "image2.png",
            "resource_service": "resource service is so and so...",
            "resource_link": "www.sample2.com",
        }]
    return expected_output