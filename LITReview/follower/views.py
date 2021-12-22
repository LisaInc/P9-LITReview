from django.shortcuts import render


def followers_page(request):
    return render(request, "follower/follower.html")
