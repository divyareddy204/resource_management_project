from abc import ABC
from abc import abstractmethod
from resource_management_auth.interactors.storages.dtos import UserDetailsDTO


class StorageInterface(ABC):

    @abstractmethod
    def create_user(self, user_name: str, password: str):
        pass

    @abstractmethod
    def get_user_details_of_given_user(self,
                                       user_name: str,
                                       password: str) -> UserDetailsDTO:
        pass

    @abstractmethod
    def validate_user_name(self, user_name: str):
        pass

    @abstractmethod
    def validate_password_for_user(self,
                                   user_name: str,
                                   password: str):
        pass
