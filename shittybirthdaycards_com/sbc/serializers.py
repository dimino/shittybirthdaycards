from rest_framework import serializers
from sbc.models import (
    Account,
    Card,
    Event,
)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ('uuid',)


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        exclude = ('uuid',)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('uuid',)
