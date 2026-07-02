from rest_framework import serializers
from documents.models.document_request import DocumentRequest
from clients.serializers.client_serializer import ClientSerializer


class DocumentRequestSerializer(serializers.ModelSerializer):
    client_details = ClientSerializer(
        source='client',
        read_only=True
    )
    client_details = ClientSerializer(
        source='client',
        read_only=True
    )
    class Meta:
        model=DocumentRequest
        fields = (
            'id',
            'title',
            'status',
            'due_date',
            'client',
            'client_details'
        )


