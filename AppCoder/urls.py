from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name="Inicio" ),
    path('cliente/',clientes, name = "Clientes" ),
    path('musica/', instrumento, name = "Instrumentos" ),
    path('pedido/', pedidos, name= "Pedidos" ),
    path('intrumentoFormulario/', intrumentoFormulario, name= "intrumentoFormulario" ),
    path("busquedaMarca/", busquedaMarca, name="busquedaMarca"),
    path("resultados/", resultados, name="ResultadosBusqueda"),

]