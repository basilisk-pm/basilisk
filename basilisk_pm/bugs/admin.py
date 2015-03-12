from django.contrib import admin
from bugs.models import Bug

# Register your models here.
class BugAdmin(admin.ModelAdmin):
    list_display = ('name','project','created_date')

admin.site.register(Bug,BugAdmin)
