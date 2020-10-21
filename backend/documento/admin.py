from django.contrib import admin
from .models import Documento
from .models import Assinatura

class AssinaturaInline(admin.TabularInline):
    model = Assinatura
    extra = 1

class AssinaturaAdmin(admin.ModelAdmin):
    # inlines = (AssinaturaInline,)
    list_display = ('id',)

class DocumentoAdmin(admin.ModelAdmin):
    # inlines = (AssinaturaInline,)
    list_display = ('id', 'nome')

admin.site.register(Assinatura, AssinaturaAdmin)
admin.site.register(Documento, DocumentoAdmin)