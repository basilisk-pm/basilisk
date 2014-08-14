from django.db import models
from django import forms
#from custom_fields import SeparatedValuesField

class Repo(models.Model):
    """Stores information about the projects repository"""
    repo_types = (('GIT','git'),('SVN','svn'))
    repo_type = models.CharField(max_length=3,choices=repo_types,default='git')
    repo_url = models.CharField(max_length=250)
    def __unicode__(self):
        return self.repo_url
    #username = models.CharField(max_length=40,default='')
    #password = forms.CharField(widget=forms.PasswordInput(),default='')


class Project(models.Model):
    """The project model keeps track of the users, code, media and bugs for iteself. Fields will be added as other apps are completed, as this model basically just keeps track of everything via the other django apps"""
    name = models.CharField(max_length=50,primary_key=True)
    start_date = models.DateTimeField('Date Started')
    repo = models.ForeignKey(Repo)
    def __unicode__(self):
        return self.name
    #users_list = custom_fields.SeparatedValuesField()
    #admin = models.ForeignKey(User)
    
    
