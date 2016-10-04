from django.conf.urls import url, include
from rest_framework import routers
from sbc import views

router = routers.DefaultRouter()
router.register(r'cards', views.CardViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
