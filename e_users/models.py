from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    user = models.ForeignKey(User)
    reading = models.DecimalField(max_digits=19,decimal_places=3)
    cost = models.DecimalField(max_digits=19,decimal_places=3)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __unicode__(self):
        return "%s" %(self.user)
