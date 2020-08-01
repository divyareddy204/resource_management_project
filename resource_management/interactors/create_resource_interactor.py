from resource_management.interactors.presenters.presenter_interface \
            import PresenterInterface
from resource_management.interactors.storages.dtos import ResourceDetailsDTO
from resource_management.interactors.storages.storage_interface \
            import StorageInterface
from resource_management.exceptions.exceptions import DuplicateResourceName

class CreateResourceInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_resource_wrapper(self,
                                resource_details_dto: ResourceDetailsDTO,
                                presenter: PresenterInterface):

        try:
            self.create_resource_interactor(resource_details_dto = resource_details_dto)
        except DuplicateResourceName:
            return presenter.raise_exception_for_duplicate_resource_name()

    def create_resource_interactor(self,
                                   resource_details_dto: ResourceDetailsDTO):

        self.storage.validate_duplicate_resource_name(
            resource_name=resource_details_dto.resource_name)

        self.storage.create_resource(resource_details_dto)
