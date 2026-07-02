import factory
from clients.models.client import Client
from accounts.models import User


class UserFactory(
    factory.django.DjangoModelFactory
):
    class Meta:
        model=User
        username=factory.Sequence(
            lambda n:f'user{n}'
        )
        email=factory.Sequence(
            lambda n:f'user{n}@gmail.com'
        )
        is_ca=True


class ClientFactory(
    factory.django.DjangoModelFactory
):
    class Meta:
        model=Client
        ca=factory.SubFactory(
            UserFactory
        )
        company_name='ABC Pvt Ltd'
        gst_number='29ABCDE1234F1Z5'
        pan_number='ABCDE1234F'
        contact_person='John'
        email='john@test.com'
        mobile='9999999999'

