from typing import List

from django.http import response

from resource_management.interactors.presenters.presenter_interface import PresenterInterface
from resource_management.interactors.storages.dtos import ResourceDetailsDTO, CompleteResourceDetailsDTO


class PresenterImplementation(PresenterInterface):

    def raise_exception_for_duplicate_resource_name(self) -> response.HttpResponse:

        from resource_management.constants.exception_messages import \
            DUPLICATE_RESOURCE_NAME
        import json
        data = {
            "response": DUPLICATE_RESOURCE_NAME[0],
            "http_status_code": 400,
            "res_status": DUPLICATE_RESOURCE_NAME[1]
        }
        """response_data = json.dumps(data)
        response_object = response.HttpResponse(response_data, 400)"""
        return data

    def raise_exception_for_invalid_resource_ids(self, err) -> response.HttpResponse:

        from resource_management.constants.exception_messages import \
            INVALID_RESOURCE_IDS
        import json
        data = {
            "response": INVALID_RESOURCE_IDS[0],
            "http_status_code": 404,
            "res_status": INVALID_RESOURCE_IDS[1]
        }
        """response_data = json.dumps(data)
        response_object = response.HttpResponse(response_data, 404)"""
        return data

    def raise_exception_for_duplicate_resource_ids(self, err) -> response.HttpResponse:

        from resource_management.constants.exception_messages import \
            DUPLICATE_RESOURCE_IDS
        import json
        data = {
            "response": DUPLICATE_RESOURCE_IDS[0],
            "http_status_code": 400,
            "res_status": DUPLICATE_RESOURCE_IDS[1]
        }
        return data

    def get_resource_details_response(
            self,
            resource_details_dtos_list: List[CompleteResourceDetailsDTO]) -> List[dict]:
        if resource_details_dtos_list:
            list_of_resource_details_dict = []
            for resource_details_dto in resource_details_dtos_list:

                resource_details_dict = {
                    "resource_id": resource_details_dto.resource_id,
                    "resource_name": resource_details_dto.resource_name,
                    "resource_link": resource_details_dto.resource_link,
                    "resource_service": resource_details_dto.resource_service,
                    "resource_pic_url": resource_details_dto.resource_pic_url,
                    "description": resource_details_dto.description
                }
                list_of_resource_details_dict.append(resource_details_dict)
            return list_of_resource_details_dict
        else:
            return []