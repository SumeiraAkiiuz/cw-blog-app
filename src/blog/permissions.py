from rest_framework.permissions import BasePermission

class IsKeeper(BasePermission):
    qoute = "You are the owner of this post."
    
    def is_obj_permission(self, request, view, obj):
        return obj.author == request.user