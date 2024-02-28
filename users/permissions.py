from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class OwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return bool(
            request.method in SAFE_METHODS or request.user == obj
        )
