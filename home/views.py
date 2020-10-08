from django.shortcuts import render
from .models import Announcement 	# this model is not being used. maybe change it as Announcements
from todo.models import ToDoList
from blog.models import BlogPost
from django.contrib.auth.models import User
from django.core.paginator import Paginator



def landing(request):
	# For accessing just the "<domain_name>/" even when the user is automatically logged-in.
	# Default will be an announcements/advertisements page.
	# "<domain_name>/home" will be the homepage linked with the "home" icon; not this one.
	user = User
	context = {
		'announcements': Announcement.objects.all(),
		'users': user.objects.order_by('-date_joined'), # try 'date_registered' to see all options
		# 'ads': 
	}
	if user:
		return render(request, 'home/wb.html', context)
	else:
		return render(request, 'home/landing.html', context)

def home(request):
	user = User
	user_list = User.objects.all()
	paginator = Paginator(user_list, 10)
	context = {
		'todos': ToDoList.objects.filter(author=request.user).order_by("finish_by"),
		'blogposts': BlogPost.objects.all().order_by("-date_posted"),
		'users': user_list
	}

	# template_folder/html_file
	return render(request, 'home/home.html', context)


# from django.views.generic import ListView

# class LandingPageListView(ListView):
# 	user = User
# 	model = Announcement
# 	template_name = 'home/landing.html'


# 	queryset = Announcement.objects.all()		# getting the 'posts' key from "context = {'posts': Post.objects.all(),}"
# 	ordering = ['-date_posted']
# 	paginate_by = 2	

# 	# def get_queryset(self):		# this defines the filter for the specific user's posts
# 	# 	user = get_object_or_404(User, username=self.kwargs.get('username'))
# 	# 	return BlogPost.objects.filter(author=user).order_by('-date_posted')


		






# as the name suggests, this page is just for testing how html+logic works...if they do.
def testing(request, username=None):
	user_list = User.objects.all()
	context = {
		'announcements': Announcement.objects.all(), # not being used // no instance created for this
		'todos': ToDoList.objects.filter(author=request.user).order_by("finish_by"),
		'blogposts': BlogPost.objects.all().order_by("-date_posted"),
		'users': user_list
	}
	return render(request, 'home/test.html')