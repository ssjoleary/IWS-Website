from django.db import models

# Create your models here.


class SpeciesManager(models.Manager):
    def get_by_natural_key(self, specname):
        return self.get(specname=specname)


class Species(models.Model):
    specname = models.CharField(max_length=200, default="editspecname", unique=True)
    specclass = models.CharField(max_length=200, default="editspecclass")
    specorder = models.CharField(max_length=200, default="editspecorder")
    specsuborder = models.CharField(max_length=200, default="editspecsuborder")
    specfamily = models.CharField(max_length=200, default="editspecfamily")
    specgenus = models.CharField(max_length=200, default="editspecgenus")
    specspecies = models.CharField(max_length=200, default="editspecspecies")
    speccommonname = models.CharField(max_length=200, default="editspeccommonname")

    def __unicode__(self):
        return self.specname

    def natural_key(self):
        return self.specname
