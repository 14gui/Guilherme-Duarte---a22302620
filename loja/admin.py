from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "quantidade_stock")
    search_fields = ("nome",)

admin.site.register(Produto, ProdutoAdmin)