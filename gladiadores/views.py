# gladiadores/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Gladiador
from .serializers import GladiatorSerializer

class GladiadorList(APIView):
    def get(self, request):
        gladiadores = Gladiador.objects.all()
        serializer = GladiatorSerializer(gladiadores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GladiatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GladiadorDetail(APIView):
    def get(self, request, pk):
        # Obtener un gladiador específico por su ID
        gladiador = get_object_or_404(Gladiador, pk=pk)
        serializer = GladiatorSerializer(gladiador)
        return Response(serializer.data)

    def put(self, request, pk):
        # Obtener un gladiador específico por su ID
        gladiador = get_object_or_404(Gladiador, pk=pk)
        
        # Pasar los nuevos datos en el cuerpo de la solicitud
        serializer = GladiatorSerializer(gladiador, data=request.data)
        
        if serializer.is_valid():
            serializer.save()  # Actualizar el gladiador con los nuevos datos
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Obtener un gladiador específico por su ID
        gladiador = get_object_or_404(Gladiador, pk=pk)
        
        # Eliminar el gladiador
        gladiador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
