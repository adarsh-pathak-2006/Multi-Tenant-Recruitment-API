from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from core.serializers import *
from core.permissions import IsCandidate, IsRecruiter, IscandidateAndRecruiter
from core.models import Company, Candidate, Experience, JobPosting, Application
from django.contrib.auth import get_user_model

User=get_user_model()


class CompanyAPI(ListCreateAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

    def get_permissions(self):
        if self.request.method=='GET':
            return [IsCandidate()]
        return [IsRecruiter()]

class CompanyAPIDetail(RetrieveUpdateDestroyAPIView):
    serializer_class=CompanySerializer
    
    def get_queryset(self):
        if self.request.user.role==User.Recruiter:
            return Company.objects.filter(recruiter=self.request.user)
        else: 
            return Company.objects.all()

    def get_permissions(self):
        if self.request.method=='GET':
            return [IsCandidate()]
        return [IsRecruiter()]

class CandidateAPI(ListCreateAPIView):
    queryset=Candidate.objects.all()
    serializer_class=CandidateSerializer

    def get_permissions(self):
        if self.request.method=='GET':
            return [IsRecruiter()]
        return [IsCandidate()]


class CandidateAPIDetail(RetrieveUpdateDestroyAPIView):
    serializer_class=CandidateSerializer

    def get_queryset(self):
        if self.request.user.role==User.Candidate:
            return Candidate.objects.filter(user=self.request.user)
        else:
            return Candidate.objects.all()

    def get_permissions(self):
        if self.request.method=='GET':
            return [IsRecruiter()]
        return [IsCandidate()]
    
class ExperienceAPI(ListCreateAPIView):
    permission_classes=[IsCandidate()]
    serializer_class=ExperienceSerializer

    def get_queryset(self):
        return Experience.objects.filter(candidate__user=self.request.user)

class ExperienceAPIDetail(RetrieveDestroyAPIView):
    permission_classes=[IsCandidate()]
    serializer_class=ExperienceSerializer

    def get_queryset(self):
        return Experience.objects.filter(candidate__user=self.request.user)
    
    
class ApplicationAPI(ListCreateAPIView):
    serializer_class=ApplicationSerializer

    def get_queryset(self):
        if self.request.user.role==User.candidate:
            return Application.objects.filter(candidate__user=self.request.user)
        else:
            return Application.objects.all()

    def get_permissions(self):
        if self.request.method=='GET':
            return [IsRecruiter()]
        return [IsCandidate()]

class ApplicationAPIDetail(RetrieveUpdateDestroyAPIView):
    serializer_class=ApplicationSerializer
    def get_queryset(self):
        if self.request.user.role==User.candidate:
            return Application.objects.filter(candidate__user=self.request.user)
        else:
            return Application.objects.all()

    def get_permissions(self):
        if self.request.method=='GET':
            return [IscandidateAndRecruiter()]
        return [IsCandidate()]


class JobpostingAPI(ListCreateAPIView):
    queryset=JobPosting.objects.all()
    serializer_class=JobPostingSerializer

    def get_permissions(self):
        if self.request.method=='GET':
            return [IscandidateAndRecruiter()]
        return [IsRecruiter()]

class JobPostingAPIDetail(RetrieveUpdateDestroyAPIView):
    serializer_class=JobPostingSerializer

    def get_queryset(self):
        if self.request.user.role==User.Recruiter:
            return JobPosting.objects.filter(company__recruiter=self.request.user)
        else:
            return JobPosting.objects.all()
    def get_permissions(self):
        if self.request.method=='GET':
            return [IscandidateAndRecruiter()]
        return [IsRecruiter()]
