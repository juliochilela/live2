from django.shortcuts import render
from .models import cambios
import requests as r
# Create your views here.
# def cambios_list_view(request):
#     cambioList = cambios.objects.all()
#     template = 'cambios-list.html'
#     return render(request, template, {'cambios': cambioList})


def cambios_list_view(request):
    cb = r.get("http://127.0.0.1:5000/api/cambios").json()
    template = 'cambios-list.html'

    return render(request, template, {'cambios': cb})