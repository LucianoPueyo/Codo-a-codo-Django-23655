from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ManyToManyField
from django.forms.models import ModelMultipleChoiceField
from django.http.request import HttpRequest
from core.models import Estudiante, Docente, Curso, Categoria, Inscripcion

"""
class CacAdminSite(admin.AdminSite):
    site_header = "Sistema de Administración del Aula virutal 2.0"
    site_title = "Administración para superusers"
    index_title = "Administración del sitio"
    empty_value_display = "vacio"
"""

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ( 'legajo', 'nombre', 'apellido')
    list_editable = ('apellido', 'nombre')
    list_display_links = ['legajo']
    search_fields = ['apellido']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field == 'estudiantes':
            kwargs["queryset"] = Estudiante.objects.filter().order_by("apellido")

        return super().formfield_for_manytomany(db_field, request, **kwargs)


"""
sitio_admin = CacAdminSite(name='cacadmin')
sitio_admin.register(Estudiante, EstudianteAdmin)
sitio_admin.register(Docente)
sitio_admin.register(Categoria)
sitio_admin.register(Inscripcion)
sitio_admin.register(Curso)
"""

admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Docente)
admin.site.register(Categoria)
admin.site.register(Inscripcion)
#admin.site.register(Curso)