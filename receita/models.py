from django.db import models

class Receita(models.Model):
    nome = models.CharField(max_length=100)
    tempo_preparo = models.IntegerField(help_text="Tempo em minutos")
    dificuldade = models.CharField(max_length=50)
    instrucoes = models.TextField()

    def __str__(self):
        return self.nome