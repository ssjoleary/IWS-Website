from django.db import models

# Create your models here.

class Species(models.Model):
	specname = models.CharField(max_length=200)
	specclass = models.CharField(max_length=200, default="Mammalia")
	specorder = models.CharField(max_length=200, default="Cetecea")

	def __unicode__(self):
		return self.specname 
