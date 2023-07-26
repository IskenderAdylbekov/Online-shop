from django.urls import path

from . import views

urlpatterns = [
    path("add/", views.add_item, name="add_item"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("<int:id>/delete/", views.delete, name="delete"),
    path("<int:id>/<slug:slug>/edit/", views.edit_item, name="edit"),
    path("browse/", views.browse, name="browse"),
]
