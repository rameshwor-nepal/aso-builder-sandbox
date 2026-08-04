from  rest_framework import serializers
from .models import *

class BusinessProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model=BusinessProblem
        fields=['id','title','description','status','created_at', 'updated_at']
        read_only_fields=['id', 'status', 'created_at', 'updated_at']
        