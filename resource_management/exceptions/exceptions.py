from typing import List


class InvalidResourceIds(Exception):
    def __init__(self, invalid_resource_ids: List[int]):
        self.invalid_resource_ids = invalid_resource_ids
        pass

class DuplicateResourceName(Exception):
    pass

class DuplicateResourceIds(Exception):
    def __init__(self, duplicate_resource_ids: List[int]):
        self.duplicate_resource_ids = duplicate_resource_ids
        pass