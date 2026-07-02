from rest_framework.parsers import MultiPartParser
from rest_framework.generics import CreateAPIView
from documents.serializers.document_serializer import DocumentSerializer
from documents.services.document_upload_service import DocumentUploadService


class UploadDocumentView(CreateAPIView):
    parser_classes=[
        MultiPartParser
    ]
    serializer_class=(
        DocumentSerializer
    )

    def perform_create(
            self,
            serializer
    ):
        DocumentUploadService.upload(
            self.request.user,
            serializer.validated_data
        )


