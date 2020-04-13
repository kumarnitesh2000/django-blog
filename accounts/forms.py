from django import forms
from django.contrib.auth.models import User
from .models import UserModel
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Avatar Name *'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))


class RegisterForm(forms.ModelForm):
    required_css_class = 'required'
    username=forms.CharField(widget=forms.TextInput({'placeholder':'Avatar Name *'}))
    email=forms.EmailField(widget=forms.EmailInput({'placeholder':'@mail.com *'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput({'placeholder':'New Password'}))
    password2=forms.CharField(label='RepeatPassword',widget=forms.PasswordInput({'placeholder':'Repeat Password'}))
    class Meta:
        model=User
        fields=('username','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password not match')
        return cd['password2']

class ImageForm(forms.ModelForm):
    class Meta:
        model=UserModel
        exclude=('user',)