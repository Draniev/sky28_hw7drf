from rest_framework.permissions import DjangoModelPermissions, SAFE_METHODS


class OwnerOrCheckDjangoPermissions(DjangoModelPermissions):
    """
    Custom model permissions to check if the user is the owner or has permission to perform actions.
    """

    def has_object_permission(self, request, view, obj):
        # If the method is in safe, you still need to change get_queryset
        # And there is no need to check permission
        if request.method in SAFE_METHODS:
            return True

        if hasattr(obj, 'owner'):
            if request.user == obj.owner:
                return True
        elif hasattr(obj, 'user'):
            if request.user == obj.user:
                return True

        # If the user is not the owner, check if they have permission to perform the action
        return super().has_object_permission(request, view, obj)
