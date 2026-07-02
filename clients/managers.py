from django.db import models


class ClientQuerySet(models.QuerySet):

    def active(self):
        return self.filter(
            is_deleted=False
        )

    def by_ca(self,ca):
        return self.filter(
            ca=ca
        )


