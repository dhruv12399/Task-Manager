# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings

# Create your models here.

# class Userprofile(models.Model):
# 	username = models.CharField(max_length = 100)
# 	email = models.EmailField(max_length = 70, unique = True)
# 	password = models.CharField(max_length = 50)

# 	def __str__(self):
# 		return self.username


class Task(models.Model):
	# user = models.ForeignKey(Userprofile, on_delete = models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	task_name = models.CharField(max_length = 100)
	added_on = models.DateTimeField(default = timezone.now)
	complete_by = models.DateTimeField('Deadline')
	completed = models.BooleanField(default = False)
	is_deleted = models.BooleanField(default = False)

	def __str__(self):
		return self.task_name

class Activity(models.Model):
	task = models.ForeignKey(Task)
	ac_type = models.IntegerField()

	def __str__(self):
		return self.task
