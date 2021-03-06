from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models


class Ticket(models.Model):
    ticket_title = models.CharField(max_length=128)
    ticket_body = models.CharField(max_length=8192, blank=True)
    img = models.ImageField(blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    has_review = models.BooleanField(default=False)

    def get_class(self):
        return "Ticket"


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    review_title = models.CharField(max_length=128)
    review_body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def get_class(self):
        return "Review"

    def get_ticket(self):
        return Ticket.objects.filter(id=self.ticket.id)[0]
