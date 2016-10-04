from rest_framework import serializers
from sbc.models import Card

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = [
            'who',
            'when',
            'street',
            'zipcode',
            'message',
        ]
