from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola Mundo parte 2")

def alumnos_listado(request):
    return HttpResponse("""
    <ul>
        <li>Pepe Gonzalez</li>
        <li>Maria Del Carril</li>
        <li>Gaston Gomez</li>
    </ul>
    """)