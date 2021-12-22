from django.shortcuts import render, redirect
from . import forms

# @login_required
def flow(request):
    return render(request, "flow/flow.html")


def posts(request):
    return render(request, "flow/user_posts.html")


def create_ticket(request):
    form = forms.create_ticket()
    if request.method == "POST":
        form = forms.create_ticket(request.POST)
        if form.is_valid():
            # traitement
            return redirect("flow/flow.html")
    return render(request, "flow/form_ticket.html", context={"form": form})


def create_review(request):
    form = forms.create_ticket()
    if request.method == "POST":
        form = forms.create_ticket(request.POST)
        if form.is_valid():
            # traitement
            return redirect("flow/flow.html")
    return render(request, "flow/form_review.html", context={"form": form})
