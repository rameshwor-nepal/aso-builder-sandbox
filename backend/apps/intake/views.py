
from rest_framework.views import APIView
from rest_framework import status

from common.responses import success_reponse
from .models import *
from .serializers import *

class BusinessProblemApiView(APIView):
    """
        Retrieve all business problems and create a new business problem.
    """
    
    authentication_classes=[]
    permission_classes=[]
    
    def get(self,request):
        business_problems=BusinessProblem.objects.all()
        serializer=BusinessProblemSerializer(business_problems, many=True)
        return success_reponse(
            data=serializer.data, 
            message="Business problems retrieved successfully."
        )
    
    def post(self, request):
        serializer=BusinessProblemSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        problem=serializer.save()
        return success_reponse(
            data=serializer.data,
            message="Business problem created successfully",
            status_code=status.HTTP_201_CREATED
        )
    