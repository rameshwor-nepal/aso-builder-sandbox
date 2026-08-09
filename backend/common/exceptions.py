
from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError, NotAuthenticated,AuthenticationFailed,PermissionDenied,NotFound
from rest_framework import status

from .responses import error_response


def custom_exception_handler(exc, context):

    # First let DRF handle the exception.
    response = exception_handler(exc, context)
    
    # If DRF doesn't know how to handle it,
    # response will be None.
    if response is None:
        return error_response(
            message="An unexpected error occurred.",
            code="INTERNAL_SERVER_ERROR",
            details={},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
             
    # Validation Error
    if isinstance(exc, ValidationError):
        return error_response(
            message="Validation failed.",
            code="VALIDATION_ERROR",
            details=response.data,
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    # Authentication failed
    if isinstance(exc, (NotAuthenticated, AuthenticationFailed)):
        return error_response(
            message="Authentication failed.",
            code="AUTHENTICATION_FAILED",
            details={},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    # Permission denied
    if isinstance(exc, PermissionDenied):
        return error_response(
            message="You do not have permission to perform this action.",
            code="PERMISSION_DENIED",
            details={},
            status_code=status.HTTP_403_FORBIDDEN,
        )

    # Resource not found
    if isinstance(exc, NotFound):
        return error_response(
            message="The requested resource was not found.",
            code="RESOURCE_NOT_FOUND",
            details={},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    # Other DRF errors
    return error_response(
        message="Request failed.",
        code="API_ERROR",
        details=response.data,
        status_code=response.status_code,
    )