from rest_framework.permissions import DjangoModelPermissions, SAFE_METHODS, DjangoObjectPermissions


class OwnerOrCheckDjangoPermissions(DjangoObjectPermissions):
    """
    Custom model permissions to check if the user is the owner or has permission to perform actions.
    """
    def has_permission(self, request, view):
        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root view when using DefaultRouter.
        print(f'check request.method: {request.method}, '
              f'request.user.is_authenticated: {request.user.is_authenticated}')
        if request.method in ('POST', 'PUT', 'DELETE', 'PATCH') and request.user.is_authenticated:
            return True

        queryset = self._queryset(view)
        perms = self.get_required_permissions(request.method, queryset.model)

        return request.user.has_perms(perms)

    def has_object_permission(self, request, view, obj):
        # If the method is in safe, you still need to change get_queryset
        # And there is no need to check permission
        if request.method in SAFE_METHODS:
            return True

        # print(f'check request.method: {request.method}, '
        #       f'request.user.is_authenticated: {request.user.is_authenticated}')
        # if request.method == 'POST' and request.user.is_authenticated:
        #     return True

        print(f'obj {obj.owner}')
        if hasattr(obj, 'owner'):
            print('проверяем аттрибут owner')
            if request.user == obj.owner:
                return True
        elif hasattr(obj, 'user'):
            if request.user == obj.user:
                return True

        # If the user is not the owner, check if they have permission to perform the action
        return super().has_object_permission(request, view, obj)
