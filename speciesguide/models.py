from django.db import models

# Create your models here.

class Species(models.Model):
	specname = models.CharField(max_length=200, default="editspecname")
	specclass = models.CharField(max_length=200, default="editspecclass")
	specorder = models.CharField(max_length=200, default="editspecorder")
	specsuborder = models.CharField(max_length=200, default="editspecsuborder")
	specfamily = models.CharField(max_length=200, default="editspecfamily")
	specgenus = models.CharField(max_length=200, default="editspecgenus")
	specspecies = models.CharField(max_length=200, default="editspecspecies")
	speccommonname = models.CharField(max_length=200, default="editspeccommonname")


	def __unicode__(self):
		return self.specname 
