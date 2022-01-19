from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import forms, models

### RÉCUPÉRER USER NAME DES FOLLOWED ET SUSCRIBED
@login_required
def followers_page(request):
    form = forms.FollowerForm()
    user_followed = [
        user_follow.followed_user
        for user_follow in models.UserFollows.objects.filter(user=request.user)
    ]
    user_subscribed = [
        user_follow.user
        for user_follow in models.UserFollows.objects.filter(followed_user=request.user)
    ]
    context = {
        "user_followed": user_followed,
        "user_subscribed": user_subscribed,
        "form": form,
    }
    if request.method == "POST":
        form = forms.FollowerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            followed = models.User.objects.filter(username=username)
            if followed:
                already_followed = models.UserFollows.objects.filter(
                    user=request.user, followed_user=followed[0]
                )
                if already_followed:
                    context["message"] = "Vous êtes déjà abonné à cet utilisateur."
                else:
                    follow = models.UserFollows(
                        user=request.user, followed_user=followed[0]
                    )
                    follow.save()
                    context["message"] = f"Vous vous êtes abonné à {username}!"
                    return render(
                        request,
                        "follower/follower.html",
                        context=context,
                    )
            else:
                context["message"] = "Cet utilisateur n'existe pas."
    return render(request, "follower/follower.html", context=context)
