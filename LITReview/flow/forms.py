from django import forms

from flow.models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = (
            "ticket_title",
            "ticket_body",
            "img",
        )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            "rating",
            "review_title",
            "review_body",
        )
