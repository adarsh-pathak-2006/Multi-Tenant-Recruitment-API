from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from core.serializers import *
from core.permissions import IsCandidate, IsRecruiter, IscandidateAndRecruiter
from core.models import Company, Candidate, Experience, JobPosting, Application
from django.shortcuts import get_object_or_404
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
        if self.request.user.role==User.RECRUITER:
            return Company.objects.filter(recruiter=self.request.user)
        else: 
            return Company.objects.all()

    def get_permissions(self):
        if self.request.method=='GET':
            return [IscandidateAndRecruiter()]
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
        if self.request.user.role==User.CANDIDATE:
            return Candidate.objects.filter(user=self.request.user)
        else:
            return Candidate.objects.all()

    def get_permissions(self):
        if self.request.method=='GET':
            return [IscandidateAndRecruiter()]
        return [IsCandidate()]
    
class ExperienceAPI(ListCreateAPIView):
    permission_classes=[IsCandidate]
    serializer_class=ExperienceSerializer

    def get_queryset(self):
        return Experience.objects.filter(candidate__user=self.request.user)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        candidate = get_object_or_404(Candidate, user=request.user)
        data['candidate'] = candidate.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        candidate = get_object_or_404(Candidate, user=self.request.user)
        serializer.save(candidate=candidate)

class ExperienceAPIDetail(RetrieveDestroyAPIView):
    permission_classes=[IsCandidate]
    serializer_class=ExperienceSerializer

    def get_queryset(self):
        return Experience.objects.filter(candidate__user=self.request.user)
    
    
class ApplicationAPI(ListCreateAPIView):
    serializer_class=ApplicationSerializer

    def get_queryset(self):
        if self.request.user.role==User.CANDIDATE:
            return Application.objects.filter(candidate__user=self.request.user)
        else:
            return Application.objects.all()

    def get_permissions(self):
        if self.request.method=='GET':
            return [IscandidateAndRecruiter()]
        return [IsCandidate()]

class ApplicationAPIDetail(RetrieveUpdateDestroyAPIView):
    serializer_class=ApplicationSerializer
    def get_queryset(self):
        if self.request.user.role==User.CANDIDATE:
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
        if self.request.user.role==User.RECRUITER:
            return JobPosting.objects.filter(company__recruiter=self.request.user)
        else:
            return JobPosting.objects.all()
    def get_permissions(self):
        if self.request.method=='GET':
            return [IscandidateAndRecruiter()]
        return [IsRecruiter()]
