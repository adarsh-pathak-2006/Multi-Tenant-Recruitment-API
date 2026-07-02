from django.contrib import admin
from core.models import Company, Experience, Candidate, JobPosting, Application, User


admin.site.register(User)
admin.site.register(Company)
admin.site.register(Experience)
admin.site.register(Candidate)
admin.site.register(JobPosting)
admin.site.register(Application)
