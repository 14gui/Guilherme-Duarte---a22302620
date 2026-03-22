from django.contrib import admin
from .models import Festival

class FestivalAdmin(admin.ModelAdmin):
    list_display = ("nome", "localizacao", "data_inicio", "data_fim")
    search_fields = ("nome", "localizacao")
    list_filter = ("localizacao",)

admin.site.register(Festival, FestivalAdmin)

# Register your models here.
