from django import forms
from django.contrib.auth.models import User
from  profiles.models import UserProfile,Snippet

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class EditForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password', required=False)
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password', required=False)
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2 and not password1:
            return None
        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('title','snippet')
