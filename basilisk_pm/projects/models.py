from django.db import models
#from profiles.models import UserProfile

# Create your models here.
class Project(models.Model):
    proj_name = models.CharField(max_length=20)
    owner  = models.ForeignKey('profiles.UserProfile')
    pub_date = models.DateTimeField(auto_now=True)
    #models.DateTimeField('Date Published')
    proj_desc = models.CharField(max_length=200)


    def __unicode__(self):
        return self.proj_name
