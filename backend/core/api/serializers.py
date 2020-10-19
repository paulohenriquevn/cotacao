from rest_framework import serializers
from core.models import Usuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email']