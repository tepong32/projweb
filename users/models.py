from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse






# remember to register to the admin.py file EVERYTIME!


class Profile(models.Model):

	# profile-related stuffs 
	user = models.OneToOneField(User, on_delete=models.CASCADE) # if the user is deleted, the profile will be deleted, too
	Male = "Male"
	Female = "Female"
	Unicorn = "Unicorn"
	gender_choice = [
		(Male, "Male"),
		(Female, "Female"),
		(Unicorn, "Unicorn")
	]
	gender = models.CharField(
		max_length=10,
		choices=gender_choice,
		default=Unicorn,
	)

	def dp_directory_path(instance, filename):
		# file will be uploaded to MEDIA_ROOT/DP_<username>/<filename> ---check settings.py. MEDIA_ROOT=media
		return '{}/DP/{}'.format(instance.user.username, filename)

	if gender == "Male":
		image = models.ImageField(default='default_m.png', upload_to=dp_directory_path) # add validation methods for uploads
	elif gender == "Female":
		image = models.ImageField(default='default_f.png', upload_to=dp_directory_path)
	else:
		image = models.ImageField(default='thehideout.jpg', upload_to=dp_directory_path)

	# these user_group will work like a status ladder // think of it like symbianize user badges
	# or use a "# of thanks/appreciation received for posts" ladder system in the future
	# 
	# user_group = group()
	# def group(self):
	# 	Pawn = "Pawn"
	# 	etc...?
	Pawn = "Pawn"
	Rook = "Rook"
	Knight = "Knight"
	Bishop = "Bishop"
	Queen = "Queen"
	King = "King"
	user_group_choices = [
		(Pawn, "Pawn"),
		(Rook, "Rook"),
		(Knight, "Knight"),
		(Bishop, "Bishop"),
		(Queen, "Queen"), # should this be removed?
		(King, "King"),
	]
	user_group = models.CharField(
		max_length=10,
		choices=user_group_choices,
		default=Pawn,
	)

	# user_group descriptions
	def title(self): 
		if self.user_group == "Pawn":
			if self.gender == "Male":
				self.title = "Average Joe"
			elif self.gender == "Female":
				self.title = "Average Jane"
			elif self.gender == "Unicorn":
				self.title = "Average Unicorn"
			return self.title

		if self.user_group == "Rook":
			if self.gender == "Male":
				self.title = "Average Joe Pro Plus"
			elif self.gender == "Female":
				self.title = "Average Jane Pro Plus"
			elif self.gender == "Unicorn":
				self.title = "Average Unicorn Pro Plus"
			return self.title

		if self.user_group == "Knight":
			if self.gender == "Unicorn":
				self.title = "A helpful Unicorn"
			else:
				self.title = "We're helping people out."
			return self.title

		if self.user_group == "Bishop":
			if self.gender == "Unicorn":
				self.title = "Powerful Unicorn. Beware."
			else:
				self.title = "A little less powerful than devs"
			return self.title

		if self.user_group == "Queen":
			if self.gender == "Female":
				self.title = "A Queen. You know what that means."
			elif self.gender == "Unicorn":
				self.title = "Queen Unicorn! MeEe-ee-ee! (what?)"
			return self.title

		if self.user_group == "King":
			self.title = "Site dev. Howrayt! ;)"
			return self.title

	
	# other socmed account links
	FB = models.CharField(max_length=80, null=True)
	IG = models.CharField(max_length=80, null=True)
	TW = models.CharField(max_length=80, null=True)

	# education / school info
	school = models.CharField(max_length=100, default="Secret!")
	FRESHMAN = 'Freshman'
	SOPHOMORE = 'Sophomore'
	JUNIOR = 'Junior'
	SENIOR = 'Senior'
	GRADUATE = 'Graduate'
	YEAR_IN_SCHOOL_CHOICES = [
		(FRESHMAN, 'Freshman'),
		(SOPHOMORE, 'Sophomore'),
		(JUNIOR, 'Junior'),
		(SENIOR, 'Senior'),
		(GRADUATE, 'Graduate'),
	]
	year_in_school = models.CharField(
		max_length=10,
		choices=YEAR_IN_SCHOOL_CHOICES,
		default=FRESHMAN,
	)
	quote = models.CharField(max_length=300)
	about_me = models.TextField(blank=True)
	date_registered = models.DateTimeField(auto_now_add=True)
	reach_me_intro = models.TextField(default="You can reach me thru: ")

	def __str__(self):
		return f"{self.user.username}'s Profile"

	def get_absolute_url(self):
		return reverse('profile', kwargs={'pk': self.pk})

	def save(self, *args, **kwargs):		# for resizing/downsizing images
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)	# open the image of the current instance
		if img.height > 50 or img.width > 50:	# for sizing-down the images to conserve memory in the server
			output_size = (100, 100)
			img.thumbnail(output_size)
			img.save(self.image.path)

