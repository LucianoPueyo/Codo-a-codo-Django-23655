from django.contrib import admin
from core.models import Estudiante, Docente, Curso, Categoria, Inscripcion


admin.site.register(Estudiante)
admin.site.register(Docente)
admin.site.register(Curso)
admin.site.register(Categoria)
admin.site.register(Inscripcion)