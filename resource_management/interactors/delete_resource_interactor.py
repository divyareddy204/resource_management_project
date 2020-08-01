from typing import List

from resource_management.interactors.presenters.presenter_interface \
            import PresenterInterface
from resource_management.interactors.storages.storage_interface \
            import StorageInterface
from resource_management.exceptions.exceptions import InvalidResourceIds, DuplicateResourceIds

class DeleteResourceInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def delete_resource_wrapper(self,
                                resource_ids: List[int],
                                presenter: PresenterInterface):

        try:
            self.delete_resource_interactor(resource_ids=resource_ids)
        except DuplicateResourceIds as err:
            return presenter.raise_exception_for_duplicate_resource_ids(err)
        except InvalidResourceIds as err:
            return presenter.raise_exception_for_invalid_resource_ids(err)

    def delete_resource_interactor(self,
                                   resource_ids: List[int]):

        self._check_for_duplicate_resource_ids(resource_ids)

        self.storage.validate_resource_ids(resource_ids)

        self.storage.delete_resource(resource_ids)

    @staticmethod
    def _check_for_duplicate_resource_ids(list_of_resource_ids):
        duplicate_resource_ids = [resource_id for resource_id in list_of_resource_ids
                              if list_of_resource_ids.count(resource_id) > 1]

        if duplicate_resource_ids:
            raise DuplicateResourceIds(duplicate_resource_ids)
