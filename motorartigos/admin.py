from django.contrib import admin
from .models import Autor, EixoTecnologia

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'biografia','email')
    search_fields = ('nome','email') 


class EixoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(Autor, AutorAdmin)
admin.site.register(EixoTecnologia,EixoAdmin)

