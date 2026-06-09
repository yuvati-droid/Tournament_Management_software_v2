from rest_framework.routers import DefaultRouter
from .views import EventViewSet
from django.urls import path
from .views import EventCreateView

urlpatterns = [
    path('events/create/', EventCreateView.as_view()),
]
router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = router.urls