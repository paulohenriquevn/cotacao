from rest_framework import serializers
from cadastros_classificacao.models import TipoDigitalizacao

class ComumSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoDigitalizacao
    fields = ('id', 'codigo', 'nome')

class TipoDigitalizacaoSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoDigitalizacao
    fields = ('id', 'codigo', 'nome')