from resource_management_auth.interactors.storages.storage_interface \
    import StorageInterface
from resource_management_auth.interactors.presenters.presenter_interface\
    import PresenterInterface
from resource_management_auth.exceptions.exceptions \
    import InvalidUserName, InvalidPassword


class UserSignUpInteractor:

    def __init__(self,
                 storage: StorageInterface):
        self.storage = storage

    def user_signup_wrapper(self,
                            user_name: str,
                            password: str,
                            presenter = PresenterInterface):
        try:
            self.user_signup_interactor(user_name=user_name,
                                        password=password)
        except InvalidUserName:
            return presenter.raise_exception_for_invalid_user_name()
        except InvalidPassword:
            return presenter.raise_exception_for_invalid_password()

    def user_signup_interactor(self,
                               user_name: str,
                               password: str):
        #print("divya******************", user_name, password)
        self.validate_user_name(user_name=user_name)
        self.validate_password(password=password)
        self.storage.create_user(user_name=user_name, password=password)

    @staticmethod
    def validate_user_name(user_name):
        is_empty_user_name = user_name == ""
        #print("********************: ", is_empty_user_name, user_name)
        if is_empty_user_name:
            raise InvalidUserName

    @staticmethod
    def validate_password(password):

        is_empty_password = password == ""
        #print("********************: ", is_empty_password, password)
        if is_empty_password:
            raise InvalidPassword
