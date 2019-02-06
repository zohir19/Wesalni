from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()

class ContactForm(forms.Form):
    fullname= forms.CharField(widget=forms.TextInput(
        attrs={"class":"form-control","placeholder":"your full name"}))
    email=forms.EmailField(widget=forms.EmailInput(
        attrs={"class":"form-control","placeholder":"your email"}) )
    content=forms.CharField(widget=forms.Textarea(
        attrs={"class":"form-control","placeholder":"talk to me"}))


class LoginForm(forms.Form):
    username= forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder":"Username", "autofocus":"True"
                                                            ,"minlength":6}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={"class":"input100", "placeholder":"Password","minlength":6}))
    remember = forms.CharField(
        widget=forms.CheckboxInput(
            attrs={"class":"input-checkbox100", "checked":True}
        )
    )
   

class RegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={"class":"input100","placeholder":"Username", "autofocus":"True"
               ,"minlength":6}))
    email=forms.EmailField(widget=forms.EmailInput(
        attrs={"class":"input100","placeholder":"E-mail"}) )
    password= forms.CharField(widget=forms.PasswordInput(
        attrs={"class":"input100","placeholder":"Password","minlength":6}))
    email_con = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class":"input100", "placeholder":"Re enter your E-mail"}
        )
    )
    phone = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={"class":"input100", "placeholder":"Phone number (+213512345678)"
                   ,"minlength":10}
        )
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={"class":"input100", "type":"date"}
        )
    )
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
        email1 = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get("email_con")

        if email2 != email1:
            raise forms.ValidationError("Email doesn't match")
        return data

    class Meta:
        model = User
        exclude = ['email_con']