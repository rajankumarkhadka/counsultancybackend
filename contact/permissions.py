from rest_framework import permissions


class IsAdminOrCreateOnly(permissions.BasePermission):
    """
    Custom permission to only allow:
    - Anyone to create (POST)
    - Only admin users to read, update, or delete
    """
    
    def has_permission(self, request, view):
        # Allow POST for everyone (create)
        if request.method == 'POST':
            return True
        
        # For all other methods (GET, PUT, PATCH, DELETE), require admin
        return request.user and request.user.is_staff
