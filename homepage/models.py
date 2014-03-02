from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include
    phone_number = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return self.user.username