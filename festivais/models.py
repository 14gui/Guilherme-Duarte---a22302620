from django.db import models

class Festival(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f'{self.nome} ({self.localizacao})'