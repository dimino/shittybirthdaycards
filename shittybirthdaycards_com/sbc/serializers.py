from rest_framework import serializers
from sbc.models import (
    Account,
    Card,
    Event,
)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        # fields = (field.name for field in Account._meta.get_fields())


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
