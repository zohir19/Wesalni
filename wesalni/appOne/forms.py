from django import forms
from appOne.models import User
from django.contrib.auth import get_user_model
from phone_field.models import PhoneFormField

User = get_user_model()

class ContactForm(forms.Form):
    fullname= forms.CharField(widget=forms.TextInput(
        attrs={"class":"form-control","placeholder":"your full name"}))
    email=forms.EmailField(widget=forms.EmailInput(
        attrs={"class":"form-control","placeholder":"your email"}) )
    content=forms.CharField(widget=forms.Textarea(
        attrs={"class":"form-control","placeholder":"talk to me"}))


class LoginForm(forms.Form):
    username= forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder":"Username", "autofocus":"True", "Required":"True"}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={"class":"input100", "placeholder":"Password"}))
   

class RegisterForm(forms.Form):
    username= forms.CharField(widget=forms.TextInput(
        attrs={"class":"form-control","placeholder":"your username"}))
    email=forms.EmailField(widget=forms.EmailInput(
        attrs={"class":"form-control","placeholder":"your email"}) )
    password= forms.CharField(widget=forms.PasswordInput(
        attrs={"class":"form-control","placeholder":"your password"}))
    password2= forms.CharField(label="Confirm password",widget=forms.PasswordInput(
        attrs={"class":"form-control","placeholder":"confirm your password"}))
    date_of_birth = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date','class':'input100','class':'form-control', "required":"true"}))
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username is taken")
        return username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email
    def clean(self):
        data=self.cleaned_data
        password=self.cleaned_data.get("password")
        password2=self.cleaned_data.get("password2")
        if password!= password2:
            raise forms.ValidationError("Passwords must match.")
        return data