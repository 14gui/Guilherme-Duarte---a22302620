from django.db import models

class Ginasio(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Socio(models.Model):
    nome = models.CharField(max_length=100)
    ginasio = models.ForeignKey(Ginasio, on_delete=models.CASCADE, related_name='socios')

    def __str__(self):
        return f'{self.nome} - {self.ginasio.nome}'