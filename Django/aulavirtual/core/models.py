from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.


# Usando un modelo Proxy ya que no agrego nuevos campos
class Persona2(User):
    class Meta:
        proxy = True

class Persona(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    email = models.EmailField(max_length=150, verbose_name="Email") 
    dni = models.IntegerField(verbose_name="Dni", unique=True)

    def clean_dni(self):
        if not (0 < self.cleaned_data['dni'] <= 99999999):
            raise ValidationError("El Dni debe ser un numero positivo de 8 digitos")
        return self.cleaned_data['dni']

    class Meta:
        abstract = True

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    def __str__(self):
        return self.nombre_completo()


class Estudiante(Persona):
    legajo = models.CharField(max_length=100, verbose_name="Legajo")
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.legajo}'

class Docente(Persona):
    cuit = models.CharField(max_length=100, verbose_name="CUIT")


class Categoria(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    descripcion = models.CharField(max_length=150, null=True, verbose_name="Descripcion del curso") 
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    cantidad_clases = models.IntegerField(verbose_name="Cantidad de clases")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante, through="Inscripcion")

    def __str__(self):
        return f"{self.nombre} {self.fecha_inicio}"


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha de inscripcion")

    def __str__(self):
        return f"{self.estudiante.nombre_completo()} - {self.curso} - {self.fecha}"
