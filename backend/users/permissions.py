from rest_framework.permissions import BasePermission
from rest_framework.permissions import BasePermission

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'SUPER_ADMIN'
        )

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['SUPER_ADMIN', 'ADMIN']


class IsScorer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'SCORER'


class IsBroadcastManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'BROADCAST_MANAGER'