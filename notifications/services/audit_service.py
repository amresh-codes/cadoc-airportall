from documents.models.audit_log import AuditLog


class AuditService:

    @staticmethod
    def log(
            document,
            user,
            action
    ):
        AuditLog.objects.create(
            document=document,
            performed_by=user,
            action=action
        )
