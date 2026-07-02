from django.urls import path
from rest_framework.routers import DefaultRouter
from documents.views.document_request_view import DocumentRequestViewSet
from documents.views.upload_document_view import UploadDocumentView


router=DefaultRouter()
router.register(
'requests',
    DocumentRequestViewSet
)
urlpatterns=router.urls
urlpatterns+=[
    path(
        'upload/',
        UploadDocumentView.as_view()
    )
]
