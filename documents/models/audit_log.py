from django.db import models
from common.models.base_model import BaseModel


class AuditLog(BaseModel):



    document=models.ForeignKey(

        'documents.Document',

        on_delete=models.CASCADE

    )



    action=models.CharField(

        max_length=100

    )



    performed_by=models.ForeignKey(

        'accounts.User',

        on_delete=models.CASCADE

    )



    remarks=models.TextField(

        blank=True

    )

