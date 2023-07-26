from django.urls import path

from . import views

app_name = "conversation"

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("<int:id>/<slug:slug>/", views.detail, name="detail"),
    path("new/<int:item_pk>/<slug:slug>/", views.new_conversation, name="new"),
]
