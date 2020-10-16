from django.db import models

# Create your models here.

# Tipo de digitalização
class TipoDigitalizacao(models.Model):
    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

# Frequência de uso
class FrequenciaUso(models.Model):
    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

# Prazos de guarda
class PrazosGuarda(models.Model):
    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

# Fase intermediária
class FaseIntermediaria(models.Model):
    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

# Destinação final
class DestinacaoFinal(models.Model):
    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

# Grau de sigio da documentação
class GrauSigioDocumentacao(models.Model):
    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=500)

    def __str__(self):
        return self.nome