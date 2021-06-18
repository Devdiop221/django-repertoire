from django.urls import path
from .views import home, about, contact_list, contact_details, new_contact, edit_contact, delete_contact

urlpatterns = [
    path("", home, name = "index"),
    path("about/", about, name = "about"),
    path("contacts/", contact_list, name = "contacts"),
    path("contacts/new/", new_contact, name = "new_contact"),
    path("contacts/<int:id>/", contact_details, name = "details"),
    path("contacts/edit/<int:id>/", edit_contact, name="edit_contact"),
    path("contacts/delete/<int:id>/",delete_contact, name="delete_contact")
]
