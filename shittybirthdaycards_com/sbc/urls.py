from django.conf.urls import url, include
from rest_framework import routers
from sbc import views

urlpatterns = [
    url(r'^cards/create/$', views.CardView.as_view(), name='card-create'),
    url(r'^cards/created/$', views.CardCreatedView.as_view(), name='card-created'),
]
