from rest_framework import viewsets
from core.models import Usuario
from .serializers import UserSerializer

class UserList(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer