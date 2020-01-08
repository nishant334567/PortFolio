from django.shortcuts import render
from .models import Job
#go and get all the jobs from database

def home(request):
	Jobs = Job.objects
	return render(request, 'jobs/home.html',{'jobs':Jobs})