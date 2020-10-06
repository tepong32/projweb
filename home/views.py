from django.shortcuts import render
from .models import Announcement 	# this model is not being used. maybe change it as Announcements
from todo.models import ToDoList
from blog.models import BlogPost
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.

def home(request):
	user_list = User.objects.all()
	paginator = Paginator(user_list, 10)
	context = {
		'announcements': Announcement.objects.all(), # not being used // no instance created for this
		'todos': ToDoList.objects.filter(author=request.user).order_by("finish_by"),
		'blogposts': BlogPost.objects.all().order_by("-date_posted"),
		'users': user_list
	}

	# template_folder/html_file
	return render(request, 'home/home.html', context)


def testing(request):
	return render(request, 'home/testing.html')


