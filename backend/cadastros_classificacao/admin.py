from django.contrib import admin

# Register your models here.
# Tipo de digitalização
from .models import TipoDigitalizacao
# Frequência de uso
from .models import FrequenciaUso
# Prazos de guarda
from .models import PrazosGuarda
# Fase intermediária
from .models import FaseIntermediaria
# Destinação final
from .models import DestinacaoFinal
# Grau de sigio da documentação
from .models import GrauSigioDocumentacao

# Tipo de digitalização
class TipoDigitalizacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

# Frequência de uso
class FrequenciaUsoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

# Prazos de guarda
class PrazosGuardaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

# Fase intermediária
class FaseIntermediariaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

# Destinação final
class DestinacaoFinalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

# Grau de sigio da documentação
class GrauSigioDocumentacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


admin.site.register(TipoDigitalizacao, TipoDigitalizacaoAdmin)
admin.site.register(FrequenciaUso, FrequenciaUsoAdmin)
admin.site.register(PrazosGuarda, PrazosGuardaAdmin)
admin.site.register(FaseIntermediaria, FaseIntermediariaAdmin)
admin.site.register(DestinacaoFinal, DestinacaoFinalAdmin)
admin.site.register(GrauSigioDocumentacao, GrauSigioDocumentacaoAdmin)
