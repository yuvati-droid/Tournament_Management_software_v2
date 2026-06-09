from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VenueViewSet, add_ground

router = DefaultRouter()
router.register(r'venues', VenueViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('venues/<int:id>/grounds/', add_ground, name='add-ground'),
]