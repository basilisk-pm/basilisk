from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='static/profile_images', blank=True)
    git_url = models.URLField(blank=True)

    def __unicode__(self):
        return self.user.username

class Snippet(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    pub_date = models.DateTimeField(auto_now=True)
    snippet = models.TextField(max_length=3000)
    title = models.CharField(max_length=30)



