from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from Inicio.models import Categoria
from .serializers import CategoriaSerializers


# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def lista_categorias(request):
    if request.method =='GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializers(categoria, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def vista_categoria (request,id):
    try:
        m =Categoria.objects.get(codigo=id)
    except Categoria.DoesNotExist:
        return Response(status= status.HTPP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CategoriaSerializers(m)
        return Response (serializer.data)
    elif request.method =='PUT':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializers(m,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        m.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
        