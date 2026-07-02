from clients.models.client import Client


class ClientService:
    @staticmethod
    def create_client(
            user,
            validated_data
    ):
        return Client.objects.create(
            ca=user,
            **validated_data
        )

    @staticmethod
    def get_clients(
            user
    ):
        return Client.objects.filter(
            ca=user
        )


