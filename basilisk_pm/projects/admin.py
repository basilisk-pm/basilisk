from django.contrib import admin
from projects.models import Project 
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('proj_name', 'owner', 'pub_date')

admin.site.register(Project,ProjectAdmin)

