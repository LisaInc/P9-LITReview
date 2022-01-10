from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms, models
from itertools import chain


@login_required
def flow(request):
    tickets = models.Ticket.objects.all()
    return render(request, "flow/flow.html", context={"tickets": tickets})


@login_required
def view_ticket(request, id):
    ticket = get_object_or_404(models.Ticket, id=id)
    return render(request, "flow/view_ticket.html", {"ticket": ticket})


@login_required
def posts(request):
    user_tickets = models.Ticket.objects.filter(user=request.user)
    user_reviews = models.Review.objects.filter(user=request.user)
    print(len(user_reviews))
    user_posts = sorted(
        chain(user_tickets, user_reviews),
        key=lambda instance: instance.time_created,
        reverse=True,
    )
    context = {
        "user_posts": user_posts,
    }
    return render(request, "flow/user_posts.html", context=context)


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
def create_review_and_ticket(request):
    form_review = forms.ReviewForm()
    form_ticket = forms.TicketForm()
    if request.method == "POST":
        form_review = forms.ReviewForm(request.POST)
        form_ticket = forms.TicketForm(request.POST, request.FILES)
        if all([form_review.is_valid(), form_ticket.is_valid()]):
            ticket = form_ticket.save(commit=False)
            ticket.user = request.user
            ticket.has_review = True
            form_ticket.save()
            review = form_review.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review = form_review.save()
            return redirect("flow")
    context = {"form_ticket": form_ticket, "form_review": form_review}
    return render(request, "flow/create_review_and_ticket.html", context=context)


@login_required
def create_review_from_ticket(request, id):
    ticket = models.Ticket.objects.get(id=id)
    form = forms.ReviewForm()
    if request.method == "POST":
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            ticket.has_review = True
            ticket.save()
            form.save()
            return redirect("flow")
    context = {"form": form, "ticket": ticket}
    return render(request, "flow/create_review_from_ticket.html", context=context)
