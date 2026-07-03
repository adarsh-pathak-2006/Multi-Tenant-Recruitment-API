from django.urls import path
from core.views import *


urlpatterns = [
    path('company/', CompanyAPI.as_view(), name='company'),
    path('company/<int:pk>/', CompanyAPIDetail.as_view(), name='company_individual'),
    path('candidate/', CandidateAPI.as_view(), name='candidate'),
    path('candidate/<int:pk>/', CandidateAPIDetail.as_view(), name='candidate_individual'),
    path('experience/', ExperienceAPI.as_view(), name='experience'),
    path('experience/<int:pk>/', ExperienceAPIDetail.as_view(), name='experience_individual'),
    path('application/', ApplicationAPI.as_view(), name='application'),
    path('application/<int:pk>/', ApplicationAPIDetail.as_view(), name='application_individual'),
    path('jobs/',JobpostingAPI.as_view(), name='jobs'),
    path('jobs/<int:pk>/', JobPostingAPIDetail.as_view(), name='jobs_individual'),
]
