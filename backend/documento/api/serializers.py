from rest_framework import serializers
from documento.models import Documento
from documento.models import Assinatura

class AssinaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assinatura
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
  assinaturas = AssinaturaSerializer(many=True)
  class Meta:
    model = Documento
    fields = '__all__'