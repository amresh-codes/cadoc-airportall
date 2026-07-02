from rest_framework.exceptions import APIException


class BusinessException(APIException):
    status_code = 400
    default_detail = "Business Validation Error"
    default_code = "business_error"


class DuplicateGSTException(BusinessException):
    default_detail = "GST already exists"


class InvalidDocumentException(BusinessException):
    default_detail = "Unsupported document"