import random
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import DocumentoSerializer
from documento.models import Documento, Assinatura

class DocumentoView(viewsets.ModelViewSet):
    serializer_class = DocumentoSerializer
    queryset = Documento.objects.all()

    def getNumeroDocumento(self):
        return ''.join(random.choice('0123456789ABCDEF') for i in range(10))

    def createAssinaturas(self, assinaturas, documento):
        for assinatura in assinaturas:
            assinaturaDocumento = Assinatura.objects.create(**assinatura)
            documento.assinaturas.add(assinaturaDocumento)

    def create(self, request, *args, **kwargs):
        # VALIDANDO DADOS ENVIADOS
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # MANIPULANDO DADOS E SALVANDO OS DADOS
        documentoData = serializer.validated_data
        assinaturas = documentoData['assinaturas']
        del documentoData['assinaturas']
        documentoData['numero'] = self.getNumeroDocumento()
        documento = Documento.objects.create(**documentoData)
        self.createAssinaturas(assinaturas, documento)
        # RETORNANDO MENSAGEM DE SUCESSO
        return Response('Documento cadastrado com sucesso', status=status.HTTP_201_CREATED)
