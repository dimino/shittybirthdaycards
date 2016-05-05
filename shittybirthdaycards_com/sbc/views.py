from rest_framework import viewsets
from sbc.models import (
    Account,
    Card,
    Event,
)
from sbc.serializers import (
    AccountSerializer,
    CardSerializer,
    EventSerializer,
)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
