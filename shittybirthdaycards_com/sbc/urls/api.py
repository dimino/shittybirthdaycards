from django.conf.urls import url, include
from rest_framework import routers
from sbc.views import api

router = routers.DefaultRouter()
router.register(r'cards', api.CardViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
