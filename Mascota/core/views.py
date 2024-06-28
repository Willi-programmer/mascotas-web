from django.shortcuts import render, HttpResponse
from django.template import loader

def index(request):
    template =loader.get_template('core/index.html')
    return HttpResponse(template.render())


def login(request):
    return render(request, "core/ingresar.html")

def registroU(request):
    return render(request, "core/registro_u.html")

