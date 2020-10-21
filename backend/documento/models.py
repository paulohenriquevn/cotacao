from django.db import models
from cadastros_classificacao.models import TipoDigitalizacao
from cadastros_classificacao.models import FrequenciaUso
from cadastros_classificacao.models import PrazosGuarda
from cadastros_classificacao.models import FaseIntermediaria
from cadastros_classificacao.models import DestinacaoFinal
from cadastros_classificacao.models import GrauSigioDocumentacao
from core.models import Usuario

class Assinatura(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    AGUARDANDO_ASSINATURA = 1
    RECUSADO = 2
    ASSINADO = 3
    STATUS_ASSINATURA = (
        (AGUARDANDO_ASSINATURA, 'sent'),
        (RECUSADO, 'paid'),
        (ASSINADO, 'ASSINADO'),
    )
    status = models.PositiveSmallIntegerField(choices=STATUS_ASSINATURA, default=AGUARDANDO_ASSINATURA)
    data = models.DateField()

    def __str__(self):
        return self.usuario.email

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
    assinaturas = models.ManyToManyField(Assinatura)