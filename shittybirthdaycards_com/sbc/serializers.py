from rest_framework import serializers
from django.conf import settings
from sbc.models import Card
from uszipcode import ZipcodeSearchEngine
from usps.addressinformation import (
    Address,
    USPSXMLError
)

import arrow


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

    def validate(self, data):
        zipcode = data['zipcode']
        when = data['when']
        street = data['street']

        zipcode_data = ZipcodeSearchEngine().by_zipcode(zipcode)

        if not zipcode_data['City']:
            raise serializers.ValidationError('US zipcode is wrong, fix it.')

        if arrow.get(arrow.utcnow()).replace(days=3).date() > arrow.get(when).to('utc').date():
            raise serializers.ValidationError("Need at least 3 days to mail the postcard.")

        usps_client = Address(settings.USPS_USERNAME)
        try:
            usps_client.validate(
                address1=street,
                city=zipcode_data['City'],
                state=zipcode_data['State']
            )
        except USPSXMLError:
            raise serializers.ValidationError("Couldn't find the street and zip combo.")

        return data
