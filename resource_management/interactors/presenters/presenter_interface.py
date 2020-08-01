from abc import ABC
from abc import abstractmethod
from typing import List

from resource_management.interactors.storages.dtos import CompleteResourceDetailsDTO


class PresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_duplicate_resource_name(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_resource_ids(self, err):
        pass

    @abstractmethod
    def raise_exception_for_duplicate_resource_ids(self, err):
        pass

    @abstractmethod
    def get_resource_details_response(self,
        resource_details_dtos_list: List[CompleteResourceDetailsDTO]) -> List[dict]:
        pass
