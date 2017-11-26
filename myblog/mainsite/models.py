# Create your models here.
from __future__ import unicode_literals

from django.db import models

# Include my timezone package
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)                # article title
    slug = models.CharField(max_length=200)                 # article URL
    body = models.TextField()                               # article context
    pub_date = models.DateTimeField(default=timezone.now)   # context publish time

    # set acticle order
    class Meta:
        ordering = ('-pub_date',)

    # provide produce data item from class , use unicode rather than str , because it's support chinese acticle
    def __unicode__(self):
        return self.title

