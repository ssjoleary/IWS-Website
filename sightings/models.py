from django.db import models
from speciesguide.models import Species

# Create your models here.	

class Sighting(models.Model):
	sub_date = models.DateTimeField('date submitted')
	species = models.ForeignKey(Species)
	animals = models.IntegerField(default=0)
	location = models.CharField(max_length=200)
	latitude = models.DecimalField(max_digits=5, decimal_places=3)
	longtitude = models.DecimalField(max_digits=5, decimal_places=3)

	def __unicode__(self):
		return self.location	