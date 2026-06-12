from django.contrib import admin

# Register your models here.
from .models import Autor, EixoTecnologia

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'biografia','email')
    search_fields = ('nome','email')


admin.site.register(Autor, AutorAdmin)

class EixoAdmin(admin.ModelAdmin):
    list_display = ('nome')
    search_fields = ('nome')

admin.site.register():

