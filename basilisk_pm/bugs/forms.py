from django.forms import ModelForm
from bugs.models import Bug,BugComment

class BugForm(ModelForm):
    class Meta:
        model = Bug
        fields = ['name','description']

class BugCommentForm(ModelForm):
    class Meta:
        model = BugComment
        fields = ['comment']

