from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        # Allow GET, HEAD, or OPTIONS requests.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Deny all other request methods.
        return False

    def has_object_permission(self, request, view, obj):
        # Allow read permissions for all requests.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Allow write permissions only if the user is the owner of the object.
        return obj.owner == request.user
