from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return (
                user.is_authenticated and user.is_admin
        )
