from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.core import serializers

import json


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    teacherSubject = models.CharField(max_length=20, blank=False)
    teacherClasses = models.CharField(max_length=100, blank=False)

    def __unicode__(self):
        return '{"%s":{"subject":"%s","classes":"[%s]"}}' % (self.user, self.teacherSubject,
                                                           self.teacherClasses)


class TimeTable(models.Model):

    user = models.ForeignKey(User)

    DateToday = models.DateField()
    Period1 = models.CharField(max_length= 10, default= "Free")
    Period2 = models.CharField(max_length= 10, default= "Free")
    Period3 = models.CharField(max_length= 10, default= "Free")
    Period4 = models.CharField(max_length= 10, default= "Free")
    Period5 = models.CharField(max_length= 10, default= "Free")
    Period6 = models.CharField(max_length= 10, default= "Free")
    Period7 = models.CharField(max_length= 10, default= "Free")

    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.user, self.DateToday, self.Period1,self.Period2,self.Period3,
                                               self.Period4,self.Period5,self.Period6,self.Period7)