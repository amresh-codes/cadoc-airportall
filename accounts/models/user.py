from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models.base_model import BaseModel


class User(AbstractUser,BaseModel):

    phone=models.CharField(

            max_length=20,
            unique=True

    )


    is_ca=models.BooleanField(
        default=False
    )


    is_client=models.BooleanField(
        default=False
    )


