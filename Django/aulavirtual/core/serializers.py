from rest_framework import serializers
from .models import Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['id', 'nombre', 'apellido', 'email', 'dni', 'legajo']