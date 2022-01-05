from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms, models


def flow(request):
    tickets = models.Ticket.objects.all()
    context = {
        "tickets": tickets,
    }
    return render(request, "flow/flow.html", context=context)


@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request, "flow/view_ticket.html", {"ticket": ticket})


@login_required
def posts(request):
    return render(request, "flow/user_posts.html")


@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            form.save()
            return redirect("flow")
    return render(request, "flow/form_ticket.html", context={"form": form})


@login_required
def create_review(request):
    form = forms.ReviewForm()
    if request.method == "POST":
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review = form.save()
            return redirect("flow")
    return render(request, "flow/form_review.html", context={"form": form})


@login_required
def create_review(request):
    form = forms.ReviewForm()
    if request.method == "POST":
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review = form.save()
            return redirect("flow")
    return render(request, "flow/form_review.html", context={"form": form})
