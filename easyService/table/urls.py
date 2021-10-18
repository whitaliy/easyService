from django.urls import path

from . import views

urlpatterns = [
    path("", views.tree, name="tree")

]