from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Password is incorrect!')
            if not user.is_active:
                raise forms.ValidationError('User is not active')
        return super(LoginForm,self).clean(*args,**kwargs)

class RegistrationForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))

    class Meta:
        model = User
        fields = [
            'username','email','password'
        ]
        widgets = {
            'username':forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter your username'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email = email)
        if email_qs.exists():
            raise forms.ValidationError('This email is already exist')
        return email
