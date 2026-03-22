from django.contrib import admin
from .models import Ginasio, Socio

class SocioInline(admin.TabularInline):
    model = Socio
    extra = 1

class GinasioAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    inlines = [SocioInline]

class SocioAdmin(admin.ModelAdmin):
    list_display = ("nome", "ginasio")
    search_fields = ("nome", "ginasio__nome")
    list_filter = ("ginasio",)

admin.site.register(Ginasio, GinasioAdmin)
admin.site.register(Socio, SocioAdmin)