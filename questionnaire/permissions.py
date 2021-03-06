from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class AnonCanGetList(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.action == 'list' or request.user and request.user.is_authenticated

# asjdkajdka
# aksldakslda
# skdlaskdlasdl
# asdklaskd'a