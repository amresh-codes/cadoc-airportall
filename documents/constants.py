
from django.db import models



class RequestStatus(models.TextChoices):


    PENDING='PENDING'


    COMPLETED='COMPLETED'


    EXPIRED='EXPIRED'



class DocumentCategory(models.TextChoices):


    PAN='PAN'

    AADHAAR='AADHAAR'

    GST='GST'

    FORM16='FORM16'

    BANK_STATEMENT='BANK_STATEMENT'

    INVOICE='INVOICE'
