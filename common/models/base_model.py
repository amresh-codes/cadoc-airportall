import uuid
from django.db import models
from common.managers import ActiveManager
from common.managers import AllManager


class BaseModel(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    is_deleted=models.BooleanField(
        default=False
    )


    class Meta:
        abstract=True

    def soft_delete(self):
        self.is_deleted = True
        self.save()

