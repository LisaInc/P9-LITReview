from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import forms, models


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
                    messages.info(request, f"Vous vous êtes abonné à {username}!")
                    return redirect("followers")

            else:
                context["message"] = "Cet utilisateur n'existe pas."
    return render(request, "follower/follower.html", context=context)


def delete_follower(request, id):
    user_to_delete = models.User.objects.get(id=id)
    print(request.user)
    follow = models.UserFollows.objects.get(
        user=request.user, followed_user=user_to_delete
    )
    if request.method == "POST":
        follow.delete()
        return redirect("followers")
    return render(request, "follower/delete_follow.html", {"user": user_to_delete})
