
from rest_framework.views import APIView
from rest_framework import generics, filters, status
from .models import BusinessProblem
from .serializers import BusinessProblemSerializer
from common.paginations import BusinessProblemPagination
from common.responses import success_response

# class BusinessProblemApiView(APIView):
#     """
#         Retrieve all business problems and create a new business problem.
#     """
    
#     authentication_classes=[]
#     permission_classes=[]
    
#     def get(self,request):
#         business_problems=BusinessProblem.objects.all()
#         serializer=BusinessProblemSerializer(business_problems, many=True)
#         return success_response(
#             data=serializer.data, 
#             message="Business problems retrieved successfully."
#         )
    
#     def post(self, request):
#         serializer=BusinessProblemSerializer(data=request.data)
        
#         serializer.is_valid(raise_exception=True)
#         problem=serializer.save()
#         return success_response(
#             data=serializer.data,
#             message="Business problem created successfully",
#             status_code=status.HTTP_201_CREATED
#         )
    

class BusinessProblemApiView(generics.ListCreateAPIView):
    """
    GET  -> list business problems (paginated, filterable, searchable, orderable)
    POST -> create a new business problem
    """
    queryset = BusinessProblem.objects.all()
    serializer_class = BusinessProblemSerializer

    authentication_classes = []
    permission_classes = []

    pagination_class = BusinessProblemPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'updated_at', 'status']
    ordering = ['-created_at']

    # We override create() because the default CreateModelMixin returns a
    # plain Response(serializer.data) — it doesn't know about your
    # success_response envelope. This is the real trade-off of generics:
    # you get list-handling for free, but still override the bits that
    # touch your custom response shape.
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return success_response(
            data=serializer.data,
            message="Business problem created successfully",
            status_code=status.HTTP_201_CREATED
        )