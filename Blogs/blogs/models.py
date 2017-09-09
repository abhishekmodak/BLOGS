# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Blog(models.Model):
    title       = models.CharField(max_length=100, unique=True)
    body        = models.TextField()
    added_date  = models.DateTimeField(db_index=True, auto_now_add=True)
    user        = models.ForeignKey(User, db_index=True)

    def __unicode__(self):
        return '%s' % self.title


class Comments(models.Model):
    blog        = models.ForeignKey(Blog, db_index=True)
    comment     = models.TextField()
    added_date  = models.DateTimeField(db_index=True, auto_now_add=True)
    user        = models.ForeignKey(User, db_index=True)


