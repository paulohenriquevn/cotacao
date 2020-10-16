from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import DocumentoSerializer
from documento.models import Documento

class DocumentoView(viewsets.ModelViewSet):
  serializer_class = DocumentoSerializer 
  queryset = Documento.objects.all()

  def create(self, request, *args, **kwargs):
    print(request.data['arquivo'])
    return super(DocumentoView, self).create(request, args, kwargs);