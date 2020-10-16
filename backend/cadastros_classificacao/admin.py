from django.contrib import admin

# Register your models here.
from .models import TipoDigitalizacao

class TipoDigitalizacaoAdmin(admin.ModelAdmin):
    list_display = ('nome')

admin.site.register(TipoDigitalizacao, TipoDigitalizacaoAdmin)