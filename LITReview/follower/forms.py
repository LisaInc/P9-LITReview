from django import forms


class FollowerForm(forms.Form):
    username = forms.CharField(label="username")
