from django.urls import path

from . import views

urlpatterns = [
    path("", views.adrlist, name="phonebook")

]