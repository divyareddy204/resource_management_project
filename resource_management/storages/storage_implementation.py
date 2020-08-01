from typing import List

from resource_management.interactors.storages.dtos \
    import ResourceDetailsDTO, CompleteResourceDetailsDTO
from resource_management.interactors.storages.storage_interface import StorageInterface
from resource_management.models.resource import Resource

class StorageImplementation(StorageInterface):

    def validate_duplicate_resource_name(self, resource_name):

        resource_obj = Resource.objects.filter(resource_name=resource_name)
        if resource_obj:
            from resource_management.exceptions.exceptions import DuplicateResourceName
            raise DuplicateResourceName

    def create_resource(self, resource_details_dto: ResourceDetailsDTO):

        Resource.objects.create(
            resource_name=resource_details_dto.resource_name,
            resource_link=resource_details_dto.resource_link,
            resource_service=resource_details_dto.resource_service,
            resource_pic_url=resource_details_dto.resource_pic_url,
            description=resource_details_dto.description
        )

    def validate_resource_ids(self, resource_ids: List[int]):

        invalid_resource_ids = []
        for resource_id in resource_ids:
            try:
                obj = Resource.objects.get(id=resource_id)
            except Resource.DoesNotExist:
                invalid_resource_ids.append(resource_id)
        if invalid_resource_ids:
            from resource_management.exceptions.exceptions import InvalidResourceIds
            raise InvalidResourceIds(invalid_resource_ids)

    def delete_resource(self, resource_ids: List[int]):
        for resource_id in resource_ids:
            Resource.objects.filter(id=resource_id).delete()

    def get_all_resources_details(self) -> List[ResourceDetailsDTO]:

        resource_objects = Resource.objects.all()
        resource_details_dtos = self.get_resource_details_dtos(resource_objects)
        return resource_details_dtos


    def get_resource_details_dtos(self, resource_objects):

        resource_details_list = []
        for resource_obj in resource_objects:
            resource_details_dto = CompleteResourceDetailsDTO(
                resource_id=resource_obj.id,
                resource_name=resource_obj.resource_name,
                resource_service=resource_obj.resource_service,
                resource_link=resource_obj.resource_link,
                resource_pic_url=resource_obj.resource_pic_url,
                description=resource_obj.description
            )
            resource_details_list.append(resource_details_dto)
        return resource_details_list
