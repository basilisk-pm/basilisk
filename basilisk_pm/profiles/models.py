from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='static/profile_images', blank=True)
    git_url = models.URLField(blank=True)

    def __unicode__(self):
        return self.user.username

