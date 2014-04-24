from django.db import models

# Create your models here.
class Repo(models.Model):
    repo_type =models.CharField(max_length=3)
    repo_url = models.CharField(max_length=300)
    repo_name = models.CharField(max_length=20)
    repo_location = models.CharField(max_length=50)
