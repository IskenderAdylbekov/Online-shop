from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from item.models import Category, Item
from .forms import SignUpForm


def index(request, category_slug=None):
    category = None
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = items.filter(category=category)
    return render(
        request,
        "shop/item/index.html",
        {"items": items, "categories": categories, "category": category},
    )


def item_detail(request, id, slug):
    item = get_object_or_404(Item, id=id, slug=slug, is_sold=False)
    categories = Category.objects.all()
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(
        id=id
    )[0:3]
    return render(
        request,
        "shop/item/detail.html",
        {"item": item, "categories": categories, "related_items": related_items},
    )


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})
