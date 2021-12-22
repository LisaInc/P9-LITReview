from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from flow.models import Ticket, Review


class create_ticket(forms.Form):
    class Meta:
        model = Ticket
        fields = (
            "title",
            "body",
            "img",
        )


class create_review(forms.Form):
    class Meta:
        model = Review
        fields = (
            "ticket",
            "rating",
            "title",
            "body",
        )
