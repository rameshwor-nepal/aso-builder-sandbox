from rest_framework.response import Response
from rest_framework import status

def success_reponse(data=None, message="Request successful", status_code=status.HTTP_200_OK):
    return Response(
        {
            "success": True,
            "message":message,
            "data":data
        },
            status=status_code
        )
    
    
def error_response(message="Something went wrong", code="Error", details=None, status_code=status.HTTP_400_BAD_REQUEST):
    return Response(
        {
            "success": False,
            "message":message,
            "error":{
                "code": code,
                "details": details or {}
            }
        },
            status=status_code
        )
