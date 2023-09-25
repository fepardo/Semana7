from rest_framework import serializers
from Inicio.models import Categoria

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['idCategoria','nombreCat']