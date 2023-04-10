from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
	"""
	Class for creating model for storing users data.
	"""
	first_name = models.CharField(max_length=30, null=False, blank=False)
	last_name = models.CharField(max_length=30, null=False, blank=False)
	email = models.EmailField(max_length=200, null=True, blank=False, unique=True)
	uid = models.EmailField(unique=True, null=False, blank=False)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(auto_now_add=True)
	password = models.CharField(max_length=128, null=True, blank=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	objects = CustomUserManager()

	def __str__(self):
		"""
		Function to return uid.
		"""
		return self.email
