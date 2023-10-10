from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from datetime import datetime
from .forms import ContactoForm 
from .models import Persona
def index(request):
    context = {
        'nombre_usuario': 'Carlos Perez',
        'fecha': datetime.now(),
        'es_instructor': True,
    }
    return render(request, "core/index.html", context)

def contacto(request):
    if request.method == "POST":
        # Instanciamos un formulario con datos
        formulario = ContactoForm(request.POST)

        # Validarlo
        if formulario.is_valid():
            # Dar de alta la info

            messages.info(request, "Consulta enviada con éxito")

            p1 = Persona(
                nombre=formulario.cleaned_data['nombre'],
                apellido=formulario.cleaned_data['apellido'],
                email=formulario.cleaned_data['mail'],
                dni=formulario.cleaned_data['dni'])
            p1.save()

            return redirect(reverse("alumnos_listado"))

    else: # GET
        formulario = ContactoForm()

    context = {
        'contacto_form': formulario
    }

    return render(request, "core/contacto.html", context)

def alumnos_listado(request):

    # Esta data en el futuro vendrá de la base de datos

    listado = Persona.objects.all()



    # listado = [
    #     'Carlos Lopez',
    #     'Maria Del Cerro',
    # ]

    context = {
        'nombre_usuario': 'Carlos Perez',
        'fecha': datetime.now(),
        'es_instructor': False,
        'listado_alumnos': listado,
        'cant_inscriptos': len(listado),
    }

    return render(request, 'core/alumnos_listado.html', context)

def alumno_detalle(request, nombre_alumno):
    return HttpResponse(
        f"""
        <h1>Bienvenid@ {nombre_alumno} </h1>
        <p>Pagina Personal de usuario</p>
        """
    )

def alumnos_historico(request, year):
    return HttpResponse(f'<h1>Historico de Alumnos del año: {year}</h1>')

def alumnos_historico_2017(request):
    return HttpResponse('<h1>Historico de Alumnos del primer año de el Aula Virtual(2017)</h1>')

def alumnos_estado(request, estado):
    return HttpResponse(f'Filtrar alumnos por estado: {estado}')
