from django.db import transaction
from documents.models.document_request import DocumentRequest
from notifications.services.notification_service import NotificationService

class DocumentRequestService:

    @staticmethod
    @transaction.atomic
    def create_request(
            user,
            validated_data
    ):
        request = DocumentRequest.objects.create(
            requested_by=user,
            **validated_data
        )
        NotificationService.create_notification(
            request.client.ca,
            "New document requested"
        )
        return request