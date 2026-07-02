from rest_framework import serializers
from clients.models.client import Client


class ClientSerializer(
        serializers.ModelSerializer
):


    class Meta:
        model=Client
        exclude = (
            'is_deleted',
            'created_at',
            'updated_at'
        )
        read_only_fields = (
            'id',
            'ca'
        )

    def validate_gst_number(self, value):
        if len(value) != 15:
            raise serializers.ValidationError(
                "GST should have 15 characters"
            )
        return value




