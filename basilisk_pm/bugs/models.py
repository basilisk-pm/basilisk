from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Bug(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=3000)
    creator  = models.ForeignKey(User, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    project = models.ForeignKey('projects.Project')

    def __unicode__(self):
        return self.name

class BugComment(models.Model):
    project = models.ForeignKey('projects.Project')
    comment = models.TextField(max_length=3000)
    created_date = models.DateTimeField(auto_now=True)
    creator  = models.ForeignKey(User, blank=True, null=True)
    bug = models.ForeignKey('Bug')
