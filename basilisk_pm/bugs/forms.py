from django.forms import ModelForm
from bugs.models import Bug

class BugForm(ModelForm):
    class Meta:
        model = Bug
        fields = ['name','description']


