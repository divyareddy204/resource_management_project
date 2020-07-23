
from resource_management_auth.interactors.storages.storage_interface \
    import StorageInterface
from resource_management_auth.models.user import User
from resource_management_auth.exceptions.exceptions import InvalidPassword, \
     InvalidUserName
from resource_management_auth.interactors.storages.dtos import UserDetailsDTO



class StorageImplementation(StorageInterface):

    def create_user(self, user_name: str, password: str):

        user = User.objects.create(username=user_name)
        user.set_password(password)
        user.save()

    def validate_password_for_user(self, user_name: str,
                                   password: str):
        try:
            user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            raise InvalidUserName

        if not user.check_password(password):
            raise InvalidPassword

    def get_user_details_of_given_user(self,
                                       user_name: str,
                                       password: str) -> UserDetailsDTO:

        try:
            user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            raise InvalidUserName

        if not user.check_password(password):
            raise InvalidPassword

        return UserDetailsDTO(user_id=user.id,
                              is_admin=user.is_admin)

    def validate_user_name(self, user_name: str):
        try:
            User.objects.get(username=user_name)
        except User.DoesNotExist:
            raise InvalidUserName
