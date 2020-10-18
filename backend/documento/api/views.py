import random
# Create your views here.
from rest_framework import viewsets
from .serializers import DocumentoSerializer
from documento.models import Documento


class DocumentoView(viewsets.ModelViewSet):
    serializer_class = DocumentoSerializer
    queryset = Documento.objects.all()

    def gerarNumeroDocumento(self):
        return ''.join(random.choice('0123456789ABCDEF') for i in range(10))

    def create(self, request, *args, **kwargs):
        request.data['numero'] = self.gerarNumeroDocumento()
        return super(DocumentoView, self).create(request, args, kwargs)
