from django.db import models

# Create your models here.

class ProblemStatuses(models.TextChoices):
    PENDING_AI="PENDING_AI","Pending AI"
    COMPLETED_AI="COMPLETED_AI","Completed AI"
    UNDER_REVIEW="UNDER_REVIEW","Under Review"

class BusinessProblem(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    status=models.CharField(max_length=20, choices=ProblemStatuses.choices, default=ProblemStatuses.PENDING_AI)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=["-created_at"]
        