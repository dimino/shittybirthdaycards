from django.conf.urls import url
from sbc import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^cards/create/$', views.CardView.as_view(), name='card-create'),
    url(r'^cards/created/$', views.CardCreatedView.as_view(), name='card-created'),
]
