from __future__ import unicode_literals

import datetime
from django.utils import timezone
from django.db import models


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	user_name = models.CharField(max_length=20)
	pub_date = models.DateTimeField('date published')
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.question_text

	# Not sure if we need it. Probably not
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	text = models.CharField(max_length=200)
	user_name = models.CharField(max_length=20)
	pub_date = models.DateTimeField('date published')
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.text