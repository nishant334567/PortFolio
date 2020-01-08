from django.shortcuts import render, get_object_or_404
#either get the post with id or throw 404
#name 'Blog' is not defined will show up if 
#below command is not imported
from .models import Blog 

def allblogs(request):
	blog = Blog.objects
	return render(request, 'blog/allblogs.html',{'blog':blog})

def detail(request,blog_id):
	detailblog=get_object_or_404(Blog, pk=blog_id)
	return render(request,'blog/detail.html',{'blog':detailblog})