
from django.contrib.auth.models import User
from django import forms
from django_recaptcha.fields import ReCaptchaField


class RecoverForm(forms.Form):
    email = forms.EmailField()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    
class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()
    captcha_field=ReCaptchaField() # import recaptha field

