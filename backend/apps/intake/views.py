
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer=BusinessProblemSerializer(data=request.data)
        
        if serializer.is_valid():
            problem=serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    