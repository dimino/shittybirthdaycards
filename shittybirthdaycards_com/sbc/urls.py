from rest_framework.routers import DefaultRouter

from sbc.views import (
    AccountViewSet,
    CardViewSet,
    EventViewSet,
)

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'cards', CardViewSet)
router.register(r'events', EventViewSet)

urlpatterns = router.urls
