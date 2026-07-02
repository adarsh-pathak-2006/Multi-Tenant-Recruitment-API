from rest_framework.serializers import ModelSerializer
from core.models import Company, Experience, Candidate, JobPosting, Application
from django.contrib.auth import get_user_model
from rest_framework.serializers import PrimaryKeyRelatedField

User=get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email']

class ExperienceSerializer(ModelSerializer):
    class Meta:
        model=Experience
        fields='__all__'

class CandidateSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    experience=ExperienceSerializer(many=True, read_only=True)
    class Meta:
        model=Candidate
        fields='__all__'

class CompanySerializer(ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'


class JobPostingSerializer(ModelSerializer):
    company=CompanySerializer(read_only=True)
    class Meta:
        model=JobPosting
        fields='__all__'

class ApplicationSerializer(ModelSerializer):
    candidate=PrimaryKeyRelatedField(read_only=True)
    job=JobPostingSerializer(read_only=True)
    class Meta:
        model=Application
        fields='__all__'

