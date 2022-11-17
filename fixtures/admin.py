from django.contrib import admin

from .models import Paises, FaseGrupos


class PaisesAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'codigo']


admin.site.register(Paises, PaisesAdmin)
admin.site.register(FaseGrupos)
