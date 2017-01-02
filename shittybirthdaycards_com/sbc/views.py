from sbc.models import Card
from sbc.serializers import CardSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, redirect

from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardView(views.APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'card_create.html'

    def get(self, request):
        serializer = CardSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = CardSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'errors': serializer.errors})
        serializer.save()
        return Response({'serializer': serializer, 'success': True})
