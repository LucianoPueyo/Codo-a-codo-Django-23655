from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alumnos/listado', views.alumnos_listado, name='alumnos_listado'),
]