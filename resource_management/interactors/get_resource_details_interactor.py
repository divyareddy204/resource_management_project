from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.interactors.storages.storage_interface \
    import StorageInterface


class GetResourceDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_resource_details_wrapper(self, presenter: PresenterInterface):

        resource_details_dtos_list = self.get_resource_details_interactor()
        return presenter.get_resource_details_response(resource_details_dtos_list)

    def get_resource_details_interactor(self):

        resource_details_dtos_list = self.storage.get_all_resources_details()
        return resource_details_dtos_list