from django.conf.urls import url, include
from rest_framework import routers
from sbc.views import ui


urlpatterns = [
    url(r'^$', ui.LandingView.as_view()),
    url(r'^cards', ui.CreateCardView.as_view()),
]
