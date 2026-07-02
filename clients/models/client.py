from django.db import models
from common.models.base_model import BaseModel
from clients.managers import ClientQuerySet


class Client(BaseModel):

    ca=models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='clients')
    company_name=models.CharField(max_length=255)
    gst_number=models.CharField(max_length=20, unique=True)
    pan_number=models.CharField(max_length=10)
    contact_person=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.CharField(max_length=20)


    class Meta:
        indexes=[
            models.Index(
                fields=['gst_number']
            )
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    'ca',
                    'gst_number'
                ],
                name='unique_client_per_ca'
            )
        ]

    objects = ClientQuerySet.as_manager()




