from django.db import models
from common.models.base_model import BaseModel
from documents.constants import RequestStatus, DocumentCategory


class DocumentRequest(BaseModel):

    client=models.ForeignKey('clients.Client', on_delete=models.CASCADE, related_name='requests')
    requested_by=models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.TextField()
    due_date=models.DateField()
    status=models.CharField(max_length=30, choices=RequestStatus.choices, default=RequestStatus.PENDING)
    category=models.CharField(max_length=30, choices=DocumentCategory.choices)


    class Meta:

        indexes = [
            models.Index(
                fields=['status']
            ),
            models.Index(
                fields=['status', 'due_date'] # search by status + due_date together
            )
        ]




