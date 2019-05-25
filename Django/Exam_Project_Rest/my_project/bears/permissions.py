from rest_framework.permissions import BasePermission

from .models import ProfileUser


class isOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            user = ProfileUser.objects.all().filter(user__pk=request.user.id)[0]
            return obj.owner == user
        except:
            return False
