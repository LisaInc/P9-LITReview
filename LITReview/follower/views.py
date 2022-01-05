from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def followers_page(request):
    return render(request, "follower/follower.html")
