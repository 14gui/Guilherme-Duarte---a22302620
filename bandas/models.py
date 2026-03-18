from django.db import models

class Genero(models.Model):
    name = models.Charfield(max_length=100)

    def __str__(self):
        return self.name