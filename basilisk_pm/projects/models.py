from django.db import models

"""Define the project model"""
class Project(models.Model):
    proj_name = models.CharField(max_length=20)
    owner  = models.ForeignKey('profiles.UserProfile')
    pub_date = models.DateTimeField(auto_now=True)
    proj_desc = models.CharField(max_length=200)
    git_url = models.URLField(blank=True)

    def __unicode__(self):
        return self.proj_name

"""Generate the path for the file to be uploaded to"""
def generate_filename(instance,filename):
    return "static/project-files/%s/%s" % (instance.project.proj_name, filename)

"""Model that assoctiates a file with a specific project"""
class ProjectFile(models.Model):
    project = models.ForeignKey(Project)
    owner = models.ForeignKey('profiles.UserProfile')
    pub_date = models.DateTimeField(auto_now=True)
    pfile = models.FileField(upload_to=generate_filename)
