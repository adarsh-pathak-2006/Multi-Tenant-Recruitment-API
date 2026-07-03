from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from core.serializers import *
from core.permissions import IsCandidate, IscandidateAndRecruiter, IsRecruiter, IsAdmin, IsAdminAndRecruiter
from core.models import Company, Candidate, Experience, JobPosting, Application
from rest_framework.permissions import IsAuthenticated


class CompanyAPI(ListCreateAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

    def get_permissions(self):
        if self.request.method=='GET':
            return [(IsCandidate)]
        return [(IsRecruiter)]

class CompanyAPIDetail(RetrieveUpdateDestroyAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

    def get_permissions(self):
        if self.request.method=='GET':
            return [(IsCandidate)]
        return [(IsRecruiter)]

class CandidateAPI(ListCreateAPIView):
    queryset=Candidate.objects.all()
    serializer_class=CandidateSerializer

    def get_permissions(self):
        if self.request.method=='GET':
            return [(IsRecruiter)]
        return [(IsCandidate)]


class CandidateAPIDetail(RetrieveUpdateDestroyAPIView):
    queryset=Candidate.objects.all()
    serializer_class=CandidateSerializer

    def get_permissions(self):
        if self.request.method=='GET':
            return [(IsRecruiter)]
        return [(IsCandidate)]
    
class ExperienceAPI(ListCreateAPIView):
    permission_classes=[(IsCandidate)]
    serializer_class=ExperienceSerializer

    def get_queryset(self):
        return Experience.objects.filter(candidate__user=self.request.user)

class ExperienceAPIDetail(RetrieveDestroyAPIView):
    permission_classes=[(IsCandidate)]
    serializer_class=ExperienceSerializer

    def get_queryset(self):
        return Experience.objects.filter(candidate__user=self.request.user)
    
    
class ApplicationAPI(ListCreateAPIView):
    queryset=Application.objects.all()
    serializer_class=ApplicationSerializer

    def get_permissions(self):
        if self.request.method=='GET':
            return [(IsAdminAndRecruiter)]
        return [(IsCandidate)]

class ApplicationAPIDetail(RetrieveUpdateDestroyAPIView):
    serializer_class=ApplicationSerializer
    def get_queryset(self):
        return Application.objects.filter(candidate__user=self.request.user)

    def get_permissions(self):
        if self.request.method=='GET':
            return [(IsAdminAndRecruiter)]
        return [(IsCandidate)]


class JobpostingAPI(ListCreateAPIView):
    queryset=JobPosting.objects.all()
    serializer_class=JobPostingSerializer

    def get_permissions(self):
        if self.request.method=='GET':
            return [(IsCandidate)]
        return [(IsRecruiter)]

class JobPostingAPIDetail(RetrieveUpdateDestroyAPIView):
    serializer_class=JobPostingSerializer

    def get_queryset(self):
        return JobPosting.objects.filter(company__recruiter=self.request.user)
    
    def get_permissions(self):
        if self.request.method=='GET':
            return [(IsCandidate)]
        return [(IsRecruiter)]
