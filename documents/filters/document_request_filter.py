from django_filters import rest_framework as filters
from documents.models.document_request import DocumentRequest


class DocumentRequestFilter(filters.FilterSet):

    class Meta:
        model = DocumentRequest
        fields = ['status']