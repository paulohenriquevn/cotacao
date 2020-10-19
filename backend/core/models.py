from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import UsuarioManager

class Usuario(AbstractUser):
    username = None
    nome = models.CharField(blank=True, max_length=100)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UsuarioManager()

    def __str__(self):
        return self.email