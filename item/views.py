from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Item, Category
from .forms import NewItemForm, EditItemForm


@login_required
def add_item(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect("detail", id=item.id, slug=item.slug)
    else:
        form = NewItemForm()
    return render(request, "item/add_item.html", {"form": form})


@login_required
def dashboard(request):
    items = Item.objects.filter(created_by=request.user)
    categories = Category.objects.all()

    return render(
        request, "item/dashboard.html", {"items": items, "categories": categories}
    )


@login_required
def delete(request, id):
    item = get_object_or_404(Item, id=id, created_by=request.user)
    item.delete()

    return redirect("dashboard")


@login_required
def edit_item(request, id, slug):
    item = get_object_or_404(Item, id=id, slug=slug, created_by=request.user)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect("detail", id=item.id, slug=item.slug)
    else:
        form = EditItemForm(instance=item)
    return render(request, "item/add_item.html", {"form": form})


def browse(request):
    query = request.GET.get("query", "")
    # category_slug = request.GET.get("category", "")
    category_id = request.GET.get("category", 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(
            category_id=category_id,
        )

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(
        request,
        "item/browse.html",
        {
            "items": items,
            "query": query,
            "categories": categories,
            # "category_slug": category_slug,
            "category_id": int(category_id),
        },
    )
