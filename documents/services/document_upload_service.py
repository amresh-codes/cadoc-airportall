from documents.models.document import Document
from notifications.services.audit_service import AuditService

class DocumentUploadService:

    @staticmethod
    def upload(
            user,
            validated_data
    ):
        document=Document.objects.create(
            uploaded_by=user,
            **validated_data
        )
        AuditService.log(
            document,
            user,
            "UPLOAD"
        )
        return document


