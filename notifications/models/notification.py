
from django.db import models


from common.models.base_model import BaseModel




class Notification(BaseModel):



    recipient=models.ForeignKey(

        'accounts.User',

        on_delete=models.CASCADE

    )



    message=models.TextField()



    is_read=models.BooleanField(

        default=False

    )


