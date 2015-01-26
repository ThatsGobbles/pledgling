import datetime

from django.db import models
from django.utils import timezone

from donors.models import Donor

class Poll(models.Model):
	text = models.CharField(max_length=200)
	create_time = models.DateTimeField(auto_now_add=True)
	start_time = models.DateTimeField()
	finish_time = models.DateTimeField()

	def __str__(self):
		return self.text

	def is_active(self):
		return self.start_time <= timezone.now() <= self.finish_time

class PollChoice(models.Model):
	poll = models.ForeignKey(Poll)
	text = models.CharField(max_length=200)

	def __str__(self):
		return self.text

class PollVote(models.Model):
	poll_choice = models.ForeignKey(PollChoice)
	donor = models.ForeignKey(Donor)
	weight = models.DecimalField(max_digits=10, decimal_places=2)
	create_time = models.DateTimeField(auto_now_add=True)

