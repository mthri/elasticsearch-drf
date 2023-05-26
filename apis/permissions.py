from rest_framework import permissions

class SearchCarPermissions(permissions.BasePermission):
    def has_permission(self, request, *args, **kwargs):
        return request.user.is_support_user


class CreateCarPermissions(permissions.BasePermission):
    def has_permission(self, request, *args, **kwargs):
        return request.user.is_support_user