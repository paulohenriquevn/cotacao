from django.contrib import admin

# Register your models here.
from .models import Usuario

# Tipo de digitalização
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

admin.site.register(Usuario, UsuarioAdmin)