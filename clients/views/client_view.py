from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from accounts.permissions import IsCA
from clients.models.client import Client
from clients.serializers import ClientSerializer
from clients.services import ClientService


class ClientViewSet(
    ModelViewSet
):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
    permission_classes = [IsCA]

    def get_queryset(self):
        return ClientService.get_clients(
            self.request.user
        )

    def create(
            self,
            request,
            *args,
            **kwargs
    ):
        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        client = ClientService.create_client(
            request.user,
            serializer.validated_data
        )

        return Response(
            ClientSerializer(client).data,
            status=status.HTTP_201_CREATED
        )


