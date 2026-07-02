from unittest.mock import patch

@patch(
    'notifications.services.notification_service.NotificationService.create_notification'
)
def test_notification_called(
        mock_notification
):
    ...
    mock_notification.assert_called_once()
