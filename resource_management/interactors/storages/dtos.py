from dataclasses import dataclass
from typing import Optional
@dataclass
class ResourceDetailsDTO:
    resource_link: str
    resource_name: str
    resource_service: str
    description: str
    resource_pic_url: str

@dataclass
class CompleteResourceDetailsDTO:
    resource_id: Optional[int]
    resource_link: str
    resource_name: str
    resource_service: str
    description: str
    resource_pic_url: str
