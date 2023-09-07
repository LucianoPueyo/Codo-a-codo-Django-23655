from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def alumnos_listado(request):
    return HttpResponse("""
    <ul>
        <li>Pepe Gonzalez</li>
        <li>Maria Del Carril</li>
        <li>Gaston Gomez</li>
    </ul>
    """)

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
