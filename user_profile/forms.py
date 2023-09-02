from django import forms
from django.forms.forms import Form
from django.core.exceptions import ValidationError
from django_editorjs import EditorJsField

from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=250, required=True)
    password = forms.CharField(max_length=250, required=True, widget=forms.PasswordInput)
    
class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=True)


class UserRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("username", "email", "password", )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        model = self.Meta.model
        user = model.objects.filter(username__iexact=username)
        
        if user.exists():
            raise forms.ValidationError("A user with that name already exists")
        
        return self.cleaned_data.get('username')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        model = self.Meta.model
        user = model.objects.filter(email__iexact=email)
        
        if user.exists():
            raise forms.ValidationError("A user with that email already exists")
        
        return self.cleaned_data.get('email')


    def clean_password(self):
        password = self.cleaned_data.get('password')
        confim_password = self.data.get('confirm_password')
        
        if password != confim_password:
            raise forms.ValidationError("Passwords do not match")

        return self.cleaned_data.get('password')


class UserProfileUpdateForm(forms.ModelForm):

    def _init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    bio = EditorJsField()

    def clean_linkedIn_url(self):
        linkedin_url = self.cleaned_data.get('linkedIn_url')
        
        if linkedin_url and not linkedin_url.startswith('https://www.linkedin.com/'):
            raise ValidationError("Please enter a valid LinkedIn URL.")
        
        return linkedin_url
    
    def clean_github_url(self):
        github_url = self.cleaned_data.get('github_url')
        
        if github_url and not github_url.startswith('https://github.com/'):
            raise ValidationError("Please enter a valid GitHub URL.")
        
        return github_url


    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email","linkedIn_url", "github_url","bio")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        model = self.Meta.model
        user = model.objects.filter(username__iexact=username).exclude(pk=self.instance.pk)
        
        if user.exists():
            raise forms.ValidationError("A user with that name already exists")
        
        return self.cleaned_data.get('username')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        model = self.Meta.model
        user = model.objects.filter(email__iexact=email).exclude(pk=self.instance.pk)
        
        if user.exists():
            raise forms.ValidationError("A user with that email already exists")
        
        return self.cleaned_data.get('email')

    def change_password(self):
        if 'new_password' in self.data and 'confirm_password' in self.data:
            new_password = self.data['new_password']
            confirm_password = self.data['confirm_password']
            if new_password != '' and confirm_password != '':
                if new_password != confirm_password:
                    raise forms.ValidationError("Passwords do not match")
                else:
                    self.instance.set_password(new_password)
                    self.instance.save()

    def clean(self):
        self.change_password()


class ProfilePictureUpdateForm(forms.Form):
    profile_image = forms.ImageField(required=True)
