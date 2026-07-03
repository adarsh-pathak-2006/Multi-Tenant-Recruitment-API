from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from core.serializers import *
from core.permissions import IsCandidate, IscandidateAndRecruiter, IsRecruiter
from core.models import Company, Candidate


class CandidateAPI(ListCreateAPIView):
    queryset=Candidate.objects.all()
    serializer_class=CandidateSerializer()

    