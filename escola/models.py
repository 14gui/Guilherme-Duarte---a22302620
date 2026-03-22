from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    numero_processo = models.IntegerField(unique=True)
    ano_letivo = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome} - Processo: {self.numero_processo}'
