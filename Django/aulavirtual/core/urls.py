from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'estudiantes', views.EstudianteViewSet, basename='estudiante')

urlpatterns = [
    path('', views.index, name='index'),
    path('api', include(router.urls)),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('contacto', views.contacto, name="contacto"),
    path('alumnos/alta', views.alta_alumno, name="alta_alumno"),
    path('alumnos/listado', views.alumnos_listado, name='alumnos_listado'),
    path('alumnos/detalle/<str:nombre_alumno>', views.alumno_detalle, name='alumnos_detalle'),
    path('alumnos/historico/2017/', views.alumnos_historico_2017, name='alumnos_historico'),
    re_path(r'alumnos/historico/(?P<year>[0-9]{4})/$', views.alumnos_historico, name='alumnos_historico'),
    path('alumnos/activos', views.alumnos_estado, {'estado': 'activo'}, name="alumnos_activos"),
    path('alumnos/inactivos', views.alumnos_estado, {'estado': 'inactivo'}, name="alumnos_inactivos"),

    path('docentes/alta', views.DocenteCreateView.as_view(), name="alta_docente"),
    path('docentes/listado', views.DocenteListView.as_view(), name="docentes_listado"),

    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
