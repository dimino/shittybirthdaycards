import logging

from sbc.models import Card
from sbc.serializers import CardSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.conf import settings

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response

log = logging.getLogger(__name__)


class CardView(views.APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'card_create.html'

    def get(self, request):
        serializer = CardSerializer()
        return Response(
            {
                'serializer': serializer,
                'stripe_public_key': settings.STRIPE_PUBLIC_KEY
            }
        )

    def post(self, request):
        serializer = CardSerializer(data=request.data)
        log.error(request.data)
        if not serializer.is_valid():
            return Response(
                {'serializer': serializer, 'errors': serializer.errors}
            )

        charge = stripe.Charge.create(
            amount=settings.POSTCARD_COST_CENTS,
            currency="usd",
            source=request.data['stripeToken'],
            description="Charge for birthday card to {}.".format(
                request.data['who']
            )
        )

        if charge['outcome']['network_status'] == 'approved_by_network':
            serializer.save(charge_id=charge.id)
            return redirect('card-created')
        else:
            errors = {
                'non_field_errors': [charge['failure_message']]
            }
            return Response({'serializer': serializer, 'errors': errors})


class CardCreatedView(TemplateView):
    template_name = 'card_created.html'
