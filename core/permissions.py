from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model


User=get_user_model()

class IsCandidate(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role==User.Candidate)
    
class IsRecruiter(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role==User.Company)
    
class IscandidateAndRecruiter(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role in [User.Company, User.Candidate])

