import arrow

from django.core.management.base import BaseCommand
from django.conf import settings

from sbc.models import Card

import lob
from uszipcode import ZipcodeSearchEngine


lob.api_key = settings.LOB_API_KEY


class Command(BaseCommand):
    def handle(self, *args, **options):
        cards_to_send = Card.objects.filter(
            when__lt=arrow.get(arrow.utcnow()).replace(days=+3).date()
        )

        for card in cards_to_send:
            print(
                'Sending card '
                '{card.id} on '
                '{card.when} to '
                '{card.street}, {card.zipcode} for '
                '{card.who} saying '
                '"{card.message}".'.format(card=card)
            )

            zipcode_data = ZipcodeSearchEngine().by_zipcode(card.zipcode)

            address = lob.Address.create(
                name=card.who,
                address_line1=card.street,
                address_city=zipcode_data['City'],
                address_state=zipcode_data['State'],
                address_country='US',
                address_zip=card.zipcode
            )

            lob.Postcard.create(
                to_address=address,
                from_address=address,
                front="""<html><body>{{who}},</body></html>""",
                data={
                    'who': card.who
                },
                message=card.message,
            )
