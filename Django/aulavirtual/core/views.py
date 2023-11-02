from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse
from datetime import datetime
from .forms import ContactoForm, AltaAlumnoForm, AltaDocenteModelForm
from .models import Estudiante, Docente
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.db import IntegrityError

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


            # p1 = Estudiante(
            #     nombre=formulario.cleaned_data['nombre'],
            #     apellido=formulario.cleaned_data['apellido'],
            #     email=formulario.cleaned_data['mail'],
            #     dni=formulario.cleaned_data['dni'])
            # p1.save()

            return redirect(reverse("alumnos_listado"))

    else: # GET
        formulario = ContactoForm()

    context = {
        'contacto_form': formulario
    }

    return render(request, "core/contacto.html", context)

def alta_alumno(request):
    context = {}

    if request.method == "POST":
        alta_alumno_form = AltaAlumnoForm(request.POST)

        if alta_alumno_form.is_valid():
            nuevo_alumno = Estudiante(
                nombre = alta_alumno_form.cleaned_data['nombre'],
                apellido = alta_alumno_form.cleaned_data['apellido'],
                email = alta_alumno_form.cleaned_data['email'],
                dni = alta_alumno_form.cleaned_data['dni'],
                legajo = alta_alumno_form.cleaned_data['legajo'],
            )

            try:
                nuevo_alumno.save()

            except IntegrityError as ie:
                messages.error(request, "Ocurrió un error al intentar dar de alta al alumno")
                return redirect(reverse("index"))

            messages.info(request, "Alumno dado de alta correctamente")
            return redirect(reverse("alumnos_listado"))
    else:
        alta_alumno_form = AltaAlumnoForm()

    context['alta_alumno_form'] = AltaAlumnoForm

    return render(request, 'core/alta_alumno.html', context)

@login_required
def alumnos_listado(request):
    listado = Estudiante.objects.all().order_by('dni')
    context = {
        'nombre_usuario': 'Carlos Perez',
        'fecha': datetime.now(),
        'es_instructor': False,
        'listado_alumnos': listado,
        'cant_inscriptos': len(listado),
    }

    return render(request, 'core/alumnos_listado.html', context)

@login_required
def alumno_detalle(request, nombre_alumno):
    return HttpResponse(
        f"""
        <h1>Bienvenid@ {nombre_alumno} </h1>
        <p>Pagina Personal de usuario</p>
        """
    )
@login_required
def alumnos_historico(request, year):
    return HttpResponse(f'<h1>Historico de Alumnos del año: {year}</h1>')

@login_required
def alumnos_historico_2017(request):
    return HttpResponse('<h1>Historico de Alumnos del primer año de el Aula Virtual(2017)</h1>')

@login_required
def alumnos_estado(request, estado):
    return HttpResponse(f'Filtrar alumnos por estado: {estado}')

class DocenteCreateView(CreateView):
    model = Docente
    #context_object_name = 'alta_docente_form'
    template_name = 'core/alta_docente.html'
    success_url = 'listado'
    # form_class = AltaDocenteModelForm
    fields = '__all__'


class DocenteListView(LoginRequiredMixin, ListView):
    model = Docente
    context_object_name = 'listado_docentes'
    template_name = 'core/docentes_listado.html'
    ordering = ['cuit']
