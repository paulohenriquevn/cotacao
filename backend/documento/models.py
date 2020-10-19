from django.db import models
from django.contrib.auth.models import User
from cadastros_classificacao.models import TipoDigitalizacao
from cadastros_classificacao.models import FrequenciaUso
from cadastros_classificacao.models import PrazosGuarda
from cadastros_classificacao.models import FaseIntermediaria
from cadastros_classificacao.models import DestinacaoFinal
from cadastros_classificacao.models import GrauSigioDocumentacao

class Documento(models.Model):
    numero = models.CharField(max_length=100)
    nome = models.CharField(max_length=500)
    descricao = models.TextField(max_length=1000)
    observacao = models.TextField(max_length=1000)
    data_cadastro = models.DateField()
    arquivo = models.FileField(blank=True, null=True)
    tipo_digitalizacao = models.ForeignKey(TipoDigitalizacao, on_delete=models.CASCADE)
    frequencia_Uso = models.ForeignKey(FrequenciaUso, on_delete=models.CASCADE)
    prazos_guarda = models.ForeignKey(PrazosGuarda, on_delete=models.CASCADE)
    fase_intermediaria = models.ForeignKey(FaseIntermediaria, on_delete=models.CASCADE)
    destinacao_final = models.ForeignKey(DestinacaoFinal, on_delete=models.CASCADE)
    grau_sigio_documentacao = models.ForeignKey(GrauSigioDocumentacao, on_delete=models.CASCADE)
    assinantes = models.ManyToManyField(User)