from django.contrib import admin

# hey i have to show up something on admin page
#if you dont want superuser to mess with database dont add

from .models import Job

admin.site.register(Job)