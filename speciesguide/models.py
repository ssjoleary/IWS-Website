from django.db import models

# Create your models here.

class Species(models.Model):
	specname = models.CharField(max_length=200)
	specclass = models.CharField(max_length=200)
	specorder = models.CharField(max_length=200)
	specsuborder = models.CharField(max_length=200)
	specfamily = models.CharField(max_length=200)
	specgenus = models.CharField(max_length=200)
	specspecies = models.CharField(max_length=200)
	speccommonname = models.CharField(max_length=200)


	def __unicode__(self):
		return self.specname 
