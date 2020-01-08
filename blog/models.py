from django.db import models
from django.conf import settings
from django.utils import timezone

class Blog(models.Model):
	#A good rule of thumb is that you use 
	#CharField when you need to limit the maximum length, TextField otherwise.
	title = models.CharField(max_length = 30)
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True, null=True)
	image = models.ImageField(upload_to='images/')
	decription = models.TextField()


	def __str__(self):
		return self.title


	def summary(self):
		return self.decription[:100]

	def pub_date_pretty(self):
		return self.published_date.strftime('%b %e %Y')