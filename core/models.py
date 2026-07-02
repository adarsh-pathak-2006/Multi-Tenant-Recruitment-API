from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    COMPANY='COMPANY'
    CANDIDATE='CANDIDATE'

    ROLE_CHOICES=[(COMPANY, 'Company'), (CANDIDATE, 'Candidate')]

    role=models.CharField(max_length=10, choices=ROLE_CHOICES)


class Company(models.Model):
    name=models.CharField(max_length=100)
    created_by=models.CharField(max_length=200)
    added_on=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Experience(models.Model):
    company=models.CharField(max_length=100)
    experience=models.PositiveIntegerField()
    skills_learned=models.TextField()

    def __str__(self):
        return self.company
    
class Candidate(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    mobileno=models.CharField(max_length=15)
    experience=models.OneToOneField(Experience, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name    

    
class JobPosting(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    stipend_min=models.PositiveIntegerField()
    stipend_max=models.PositiveIntegerField()
    mode=models.CharField(max_length=10, choices=[('REMOTE', 'REMOTE'), ('ON-SITE', 'ON-SITE')])
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.title[:80]
    
class Application(models.Model):
    candidate=models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job=models.ManyToManyField(JobPosting)
    status=models.CharField(max_length=10, choices=[('APPLIED','APPLIED'), ('SCREENING', 'SCREENING'), ('INTERVIEWING', 'INTERVIEWING')])
    resume_url=models.URLField()
    applied_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.candidate.user.first_name