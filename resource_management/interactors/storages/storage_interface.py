from abc import ABC, abstractmethod
from typing import List

from resource_management.interactors.storages.dtos import ResourceDetailsDTO, CompleteResourceDetailsDTO


class StorageInterface(ABC):

    @abstractmethod
    def validate_duplicate_resource_name(self, resource_name: str):
        pass

    @abstractmethod
    def create_resource(self, resource_details_dto: ResourceDetailsDTO):
        pass

    @abstractmethod
    def validate_resource_ids(self, resource_ids: List[int]):
        pass

    @abstractmethod
    def delete_resource(self, resource_ids: List[int]):
        pass

    @abstractmethod
    def get_all_resources_details(self) -> List[CompleteResourceDetailsDTO]:
        pass
