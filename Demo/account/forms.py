from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
class RegisterForm(forms.ModelForm):

    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username","email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("no")
        return cd['password2']

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ("School","Class","phone","SchoolNumber","RealName","photo")

class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)