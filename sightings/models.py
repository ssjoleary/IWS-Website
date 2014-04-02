from django.db import models
from speciesguide.models import Species

# Create your models here.	


class Sighting(models.Model):
    sub_date = models.CharField(max_length=200, default='date submitted')
    species = models.ForeignKey('speciesguide.Species')
    animals = models.IntegerField(default=0)
    location = models.CharField(max_length=200, default='editLocation')
    latitude = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    longitude = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    name = models.CharField(max_length=200, default='observer name')

    def __unicode__(self):
        return self.location