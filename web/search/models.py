# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
import json


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    firstname = models.CharField(max_length=45, blank=True)
    gender = models.CharField(max_length=45, blank=True)
    photo = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.user_id + " " + self.firstname

    def as_dict(self):
        user_dict = {}
        user_dict['id'] = self.user_id
        user_dict['firstname'] = self.firstname
        user_dict['gender'] = self.gender
        user_dict['photo'] = json.loads(self.photo)
        return user_dict

    class Meta:
        db_table = 'users'


class Venue(models.Model):
    venue_id = models.CharField(primary_key=True, max_length=60)
    name = models.CharField(max_length=45, blank=True)
    location = models.CharField(max_length=1000, blank=True)
    menu = models.CharField(max_length=1000, blank=True)
    stats = models.CharField(max_length=1000, blank=True)
    categories = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.venue_id + " " + self.name

    def as_dict(self):
        pass

    class Meta:
        db_table = 'venues'


class Tip(models.Model):
    tip_id = models.CharField(primary_key=True, max_length=50)
    canonicalurl = models.CharField(db_column='canonicalUrl',
                                    max_length=300,
                                    blank=True)  # Field name made lowercase.
    likes = models.IntegerField(blank=True, null=True)
    likes_content = models.CharField(max_length=2000, blank=True)
    text = models.CharField(max_length=2000, blank=True)
    user = models.ForeignKey(User, blank=True, null=True)
    venue = models.ForeignKey(Venue, blank=True, null=True)

    def __unicode__(self):
        return self.tip_id

    def as_dict(self):
        tip_dict = {}
        tip_dict['id'] = self.tip_id
        tip_dict['likes'] = self.likes
        tip_dict['likes_content'] = json.loads(self.likes_content)
        tip_dict['text'] = self.text
        tip_dict['user'] = self.user.as_dict()
        return tip_dict

    class Meta:
        db_table = 'tips'
