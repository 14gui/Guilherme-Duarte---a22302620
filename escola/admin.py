from django.contrib import admin
from .models import Aluno

class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "numero_processo", "ano_letivo")
    search_fields = ("nome", "numero_processo")

admin.site.register(Aluno, AlunoAdmin)