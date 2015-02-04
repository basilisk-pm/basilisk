from django.db import models

# Create your models here.
class Project(models.Model):
    proj_name = models.CharField(max_length=20)
    owner = models.CharField(max_length=10)
    pub_date = models.DateTimeField('Date Published')
    proj_desc = models.CharField(max_length=200)
