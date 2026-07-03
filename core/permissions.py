from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model


User=get_user_model()

class IsCandidate(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role==User.CANDIDATE)
    
class IsRecruiter(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role==User.RECRUITER)
    
class IscandidateAndRecruiter(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role in [User.RECRUITER, User.CANDIDATE])

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role==User.ADMIN)
    
class IsAdminAndRecruiter(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role in [User.ADMIN , User.RECRUITER])