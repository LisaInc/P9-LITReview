from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from itertools import chain

from . import forms, models
from follower.models import UserFollows


@login_required
def flow(request):
    user_followed = [
        follow.followed_user for follow in UserFollows.objects.filter(user=request.user)
    ]
    user_followed.append(request.user)
    tickets_without_review = models.Ticket.objects.filter(
        user__in=user_followed, has_review=False
    )
    reviews = models.Review.objects.filter(user__in=user_followed)
    posts = sorted(
        chain(tickets_without_review, reviews),
        key=lambda instance: instance.time_created,
        reverse=True,
    )
    reviews_tickets = {review.id: review.get_ticket() for review in reviews}
    print(reviews_tickets[reviews[0].id])
    return render(
        request,
        "flow/flow.html",
        context={"posts": posts, "reviews_tickets": reviews_tickets},
    )


@login_required
def user_posts(request):
    user_tickets = models.Ticket.objects.filter(user=request.user)
    user_reviews = models.Review.objects.filter(user=request.user)
    user_posts = sorted(
        chain(user_tickets, user_reviews),
        key=lambda instance: instance.time_created,
        reverse=True,
    )
    context = {
        "posts": user_posts,
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


def update_post(request, id, post_type):
    if post_type == "Ticket":
        post = models.Ticket.objects.get(id=id)
        form = forms.TicketForm(instance=post)
    else:
        post = models.Review.objects.get(id=id)
        form = forms.ReviewForm(instance=post)
    if request.method == "POST":
        if post_type == "Ticket":
            form = forms.TicketForm(request.POST, instance=post)
        else:
            form = forms.ReviewForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts")
    return render(request, "flow/post_update.html", {"form": form})


def delete_post(request, id, post_type):
    if post_type == "Ticket":
        post = models.Ticket.objects.get(id=id)
    else:
        post = models.Review.objects.get(id=id)
    if request.method == "POST":
        post.delete()
        return redirect("posts")
    return render(request, "flow/post_delete.html", {"post": post})
