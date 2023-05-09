from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('formulario/', views.formulario, name='form'),
    path('registrarAlumno/', views.FormularioAlumnoView.index, name='registrar'),
    path('guardarAlumno/', views.FormularioAlumnoView.procesar_formulario, name='guardar'),
    path('listaAlumnos/', views.FormularioAlumnoView.listar_alumnos, name='listar'),
    path('editarAlumno/<int:id_alumno>', views.FormularioAlumnoView.edit, name='editar'),
    path('actualizarAlumno/<int:id_alumno>', views.FormularioAlumnoView.actualizar, name='actualizar'),
    path('eliminarAlumno/<int:id_alumno>', views.FormularioAlumnoView.delete, name='eliminar'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)