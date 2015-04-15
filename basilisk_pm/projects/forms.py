from django import forms
from django.forms import ModelForm
from projects.models import Project, ProjectFile

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['proj_name','proj_desc']

class EditProjectForm(forms.Form):
    git_url = forms.URLField(label='Git URL', required = False )
    proj_desc = forms.CharField(label='Project Description')
    
class ProjectFileForm(ModelForm):
    class Meta:
        model = ProjectFile
        fields = ['pfile']

