from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import TipoDigitalizacaoSerializer
from .models import TipoDigitalizacao

class TipoDigitalizacaoController(viewsets.ModelViewSet):
  serializer_class = TipoDigitalizacaoSerializer 
  queryset = TipoDigitalizacao.objects.all()
