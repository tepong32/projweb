from django.db import models
from django.utils import timezone	# for "default" argument in DateTimeField
from django.contrib.auth.models import User
from django import forms	# for pagedown


# each class is going to be "it's own table in the database."

class Announcement(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True) #you can use "(default=timezone.now)" instead but the timezone import is needed
	date_modified = models.DateTimeField(auto_now=True) # shows the actual time the post was modified // everytime it is modified
	author = models.ForeignKey(User, on_delete=models.CASCADE) # ForeignKey is for relationship with another model

	def __str__(self):			# for printing the title of the post whenever it gets called in the query (using python shell)
		return self.title

	def get_absolute_url(self):
		return reverse('announcement-detail', kwargs={'pk': self.pk})

	def get_markdown(self):
		content = self.content
		markdown_text = markdown(content)
		return mark_safe(markdown_text)


