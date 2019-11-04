from django.db import models
from django.conf import settings
from django.urls import reverse
from django.conf.urls import url
# Create your models here.
class message(models.Model):

	name 	 = models.CharField(max_length=120)
	title 	 = models.CharField(max_length=120)
	slug 	 = models.SlugField()
	key      = models.CharField(max_length=120)
	text     = models.TextField()
	text2    = models.TextField(default=0)
	active 	 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('message-detail', kwargs={'slug': self.slug})

class UserAccount(models.Model):

	user        = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	first_name  = models.CharField(max_length=200)
	last_name   = models.CharField(max_length=200)
	email       = models.EmailField()
	active      = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('account_view', kwargs={'user': user.username})