from django.db import models
from django.db.models import Sum

class Donor(models.Model):
	email = models.EmailField(max_length=254, unique=True)
	handle = models.CharField(max_length=200)
	create_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{handle} ({email})".format(handle=self.handle, email=self.email)

	def total_donated(self):
		return Donation.objects.filter(donor=self).aggregate(Sum('amount'))

class Donation(models.Model):
	donor = models.ForeignKey(Donor)
	amount = models.DecimalField(max_digits=7, decimal_places=2)
	create_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{amount} by {donor}".format(amount=self.amount, donor=self.donor)

