from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import IntrumentoFormulario
from AppCoder.models import *

# Create your views here.

def inicio(request):

    return render(request, "AppCoder/inicio.html")

def clientes(request):

    return render(request, "AppCoder/cliente.html")

def instrumento(request): 

    return render(request, "AppCoder/instrumento.html")

def pedidos(request): 

    return render(request, "AppCoder/pedido.html")


def intrumentoFormulario(request):

    if request.method == "POST":

        formulario1 = IntrumentoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            instrumento = Instrumento(instrumento=info["instrumento"],
                                      marca=info["marca"])

            instrumento.save()

            return render(request, "AppCoder/inicio.html")
        
    else:

        formulario1 = IntrumentoFormulario()

    return render(request, "AppCoder/intrumentoFormulario.html", {"form1":formulario1})

def busquedaMarca(request):
    return render(request, "AppCoder/inicio.html")

def resultados (request):

    if request.GET['marca']:

        marca = request.GET['marca']
        instrumentos = Instrumento.objects.filter(marca__icontains=marca)

        return render(request, "AppCoder/inicio.html", {"instrumentos":instrumentos, "marca":marca})
    
    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)