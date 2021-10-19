from .models import MAN
from django.shortcuts import render




def adrlist(request):
    latestman = MAN.objects.all()
    return render(request, 'phonebook.html',{"MANS":latestman})