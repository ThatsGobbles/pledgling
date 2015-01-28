import datetime

from django.db import models
from django.utils import timezone
from django.db.models import Sum, Count

from donors.models import Donor

class Poll(models.Model):
	text = models.CharField(max_length=200)
	create_time = models.DateTimeField(auto_now_add=True)
	start_time = models.DateTimeField()
	finish_time = models.DateTimeField()

	def __str__(self):
		return self.text

	def choices(self):
		return PollChoice.objects.filter(poll=self)

	def num_choices(self):
		return self.choices().count()

	def ranked_choices(self):
		return self.choices().annotate(choice_weight=Sum('pollvote__weight')).order_by('-choice_weight')

	def winning_choice(self):
		for choice in self.ranked_choices():
			return choice

		return None

	#Entry.objects.filter(id__in=[1, 3, 4])

	def total_weight(self):
		return self.choices().annotate(choice_weight=Sum('pollvote__weight')).aggregate(Sum('choice_weight'))

	def total_votes(self):
		return self.choices().annotate(choice_votes=Count('pollvote')).aggregate(Sum('choice_votes'))

	def is_active(self):
		return self.num_choices() >= 2 and self.start_time <= timezone.now() <= self.finish_time

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

