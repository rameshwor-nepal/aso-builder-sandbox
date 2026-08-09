from  rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import BusinessProblem

class BusinessProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model=BusinessProblem
        fields=['id','title','description','status','created_at', 'updated_at']
        read_only_fields=['id', 'status', 'created_at', 'updated_at']
        
    def validate_title(self, value):
        value=value.strip()
        
        if len(value) < 10:
            raise ValidationError("Title must be at least 10 character long.")
        
        if len(value.split()) < 2:
            raise ValidationError("Title must be at least 2 words")
        
        if value.isdigit():
            raise ValidationError("Title cannot contain only numbers")
        
        return value

    def validate_description(self, value):
        value = value.strip()

        if len(value) < 50:
            raise ValidationError(
                "Description must be at least 50 characters long."
            )
        return value
    
    def validate(self, attributes):
        title = attributes.get("title", "").strip().lower()
        description = attributes.get("description", "").strip().lower()
        
        if title == description:
            raise ValidationError({
                "description": ( "Description must provide more detail than the title.")
            })
        
        return attributes