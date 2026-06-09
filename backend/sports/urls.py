from rest_framework.routers import DefaultRouter
from .views import SportViewSet

router = DefaultRouter()
router.register(r'sports', SportViewSet)

urlpatterns = router.urls