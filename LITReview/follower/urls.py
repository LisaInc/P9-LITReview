from django.urls import path
from . import views

urlpatterns = {
    path("followers", views.followers_page, name="followers"),
}
