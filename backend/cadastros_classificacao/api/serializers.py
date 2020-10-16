from rest_framework import serializers
from .models import TipoDigitalizacao

class TipoDigitalizacaoSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoDigitalizacao
    fields = ('id', 'nome')