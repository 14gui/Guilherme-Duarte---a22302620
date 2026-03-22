from django.contrib import admin
from .models import Receita

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tempo_preparo", "dificuldade")
    search_fields = ("nome",)
    list_filter = ("dificuldade",)

admin.site.register(Receita, ReceitaAdmin)