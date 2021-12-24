from django.urls import path
from . import views

urlpatterns = [
    path("", views.flow, name="aa"),
    path("form_review/", views.create_review, name="form_review"),
    path("form_ticket/", views.create_ticket, name="form_ticket"),
    path("posts/", views.posts, name="posts"),
]
