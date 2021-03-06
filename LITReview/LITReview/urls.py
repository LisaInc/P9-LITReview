"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import flow.views
import follower.views
import authentication.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", authentication.views.login_page, name="login"),
    path("signup", authentication.views.signup_page, name="signup"),
    path("logout/", authentication.views.logout_user, name="logout"),
    path("flow", flow.views.flow, name="flow"),
    path(
        "flow/<int:id>/add_review/",
        flow.views.create_review_from_ticket,
        name="create_review_from_ticket",
    ),
    path(
        "flow/create_review_and_ticket",
        flow.views.create_review_and_ticket,
        name="create_review_and_ticket",
    ),
    path(
        "flow/<slug:post_type>/<int:id>/delete/",
        flow.views.delete_post,
        name="delete_post",
    ),
    path(
        "flow/<slug:post_type>/<int:id>/update/",
        flow.views.update_post,
        name="update_post",
    ),
    path("flow/form_ticket/", flow.views.create_ticket, name="form_ticket"),
    path("flow/posts", flow.views.user_posts, name="posts"),
    path("followers", follower.views.followers_page, name="followers"),
    path(
        "follower/<int:id>/delete/",
        follower.views.delete_follower,
        name="delete_follower",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
