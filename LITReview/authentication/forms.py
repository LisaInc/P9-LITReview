from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d’utilisateur")
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")
