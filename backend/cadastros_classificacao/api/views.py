from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ComumSerializer
from cadastros_classificacao.models import TipoDigitalizacao
from cadastros_classificacao.models import FrequenciaUso
from cadastros_classificacao.models import PrazosGuarda
from cadastros_classificacao.models import FaseIntermediaria
from cadastros_classificacao.models import DestinacaoFinal
from cadastros_classificacao.models import GrauSigioDocumentacao

class TipoDigitalizacaoView(viewsets.ModelViewSet):
  serializer_class = ComumSerializer 
  queryset = TipoDigitalizacao.objects.all()

class FrequenciaUsoView(viewsets.ModelViewSet):
  serializer_class = ComumSerializer 
  queryset = FrequenciaUso.objects.all()

class PrazosGuardaView(viewsets.ModelViewSet):
  serializer_class = ComumSerializer 
  queryset = PrazosGuarda.objects.all()

class FaseIntermediariaView(viewsets.ModelViewSet):
  serializer_class = ComumSerializer 
  queryset = FaseIntermediaria.objects.all()

class DestinacaoFinalView(viewsets.ModelViewSet):
  serializer_class = ComumSerializer 
  queryset = DestinacaoFinal.objects.all()

class GrauSigioDocumentacaoView(viewsets.ModelViewSet):
  serializer_class = ComumSerializer 
  queryset = GrauSigioDocumentacao.objects.all()
