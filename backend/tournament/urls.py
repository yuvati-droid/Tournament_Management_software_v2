from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('players.urls')),
    path('api/', include('teams.urls')),
    path('api/', include('matches.urls')),
    path('api/', include('tournaments.urls')),
    path('api/', include('events.urls')),
    path('api/', include('sports.urls')),
    # path('api/', include('users.urls')),
    path('api/auth/', include('rest_framework.urls')),  # For browsable API login/logout

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]