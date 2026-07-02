from django.db.models.signals import post_save
from django.dispatch import receiver
from documents.models.document_request import DocumentRequest
from notifications.services.notification_service import NotificationService


@receiver(post_save, sender=DocumentRequest)
def document_request_created(
        sender,
        instance,
        created,
        **kwargs
):
    if created:
        NotificationService.create_notification(
            instance.client.ca,
            "Document Request Created"
        )
