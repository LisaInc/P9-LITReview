from django import forms
from django.forms import fields
from flow.models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = (
            "title",
            "body",
            "img",
        )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            "rating",
            "title",
            "body",
        )
