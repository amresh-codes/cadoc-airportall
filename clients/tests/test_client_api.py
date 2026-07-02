import pytest
from rest_framework.test import APIClient
from clients.tests.factories import UserFactory

@pytest.mark.django_db
def test_create_client():
    api_client=APIClient()
    user=UserFactory()
    api_client.force_authenticate(
        user=user
    )
    payload={
        'company_name':'XYZ Pvt Ltd',
        'gst_number':'29ABCDE1234F1Z5',
        'pan_number':'ABCDE1234F',
        'contact_person':'Rahul',
        'email':'rahul@test.com',
        'mobile':'9999999999'
    }
    response=api_client.post(
        '/api/clients/',
        payload
    )
    assert response.status_code==201
