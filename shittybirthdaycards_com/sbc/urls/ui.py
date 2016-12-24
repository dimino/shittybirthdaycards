from django.conf.urls import url, include
from rest_framework import routers
from sbc.views import ui


urlpatterns = [
    url(r'^$', ui.IndexView.as_view()),
]
