from django.conf.urls import url, include

urlpatterns = [
    url(r'', include('sbc.urls.ui')),
    url(r'^api/v1/', include('sbc.urls.api')),
]
