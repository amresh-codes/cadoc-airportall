
from django.db import models


from common.models.base_model import BaseModel




class Document(BaseModel):



    request=models.ForeignKey(


        'documents.DocumentRequest',


        on_delete=models.CASCADE,


        related_name='documents'


    )




    file=models.FileField(


        upload_to='documents/'


    )



    uploaded_by=models.ForeignKey(


        'accounts.User',


        on_delete=models.CASCADE


    )




    uploaded_at=models.DateTimeField(

        auto_now_add=True

    )


