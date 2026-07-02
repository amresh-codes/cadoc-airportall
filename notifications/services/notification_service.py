from notifications.models.notification import Notification


class NotificationService:

    @staticmethod
    def create_notification(
            user,
            message
    ):
        Notification.objects.create(
            recipient=user,
            message=message
        )

