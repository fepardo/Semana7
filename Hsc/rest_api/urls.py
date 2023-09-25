from django.urls import path
from rest_framework.views import lista_categorias, vista_categoria

urlpatterns =[
    path('lista_categorias/',lista_categorias, name="lista_categorias"),
    path('vista_categoria/<id>',vista_categoria, name="vista_categoria"),
]