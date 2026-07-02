from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from accounts.permissions import IsCA
from common.pagination import CustomPagination
from documents.models.document_request import DocumentRequest
from documents.filters.document_request_filter import DocumentRequestFilter
from documents.serializers.document_request_serializer import DocumentRequestSerializer


class DocumentRequestViewSet(ModelViewSet):

    serializer_class = DocumentRequestSerializer
    permission_classes = [IsCA]
    pagination_class = CustomPagination
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_class = DocumentRequestFilter

    search_fields = [
        'title',
        'description'
    ]
    ordering_fields = [
        'due_date',
        'created_at'
    ]
    ordering = [
        '-created_at'
    ]

    def get_queryset(self):
        return (
            DocumentRequest.objects
            .select_related(
                'client',
                'requested_by'
            )
            .prefetch_related(
                'documents'
            )
            .filter(
                client__ca=self.request.user
            )
        )