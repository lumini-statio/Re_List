from urllib import request
from django.http import HttpRequest
from django.shortcuts import render
from .models import Alumno
from .forms import FormularioAlumno

def home(request):
    template_name = 'curso/home.html'
    return render(request, template_name=template_name)
    
def formulario(request):
    template_name = 'curso/formulario.html'
    return render(request, template_name=template_name)

class FormularioAlumnoView(HttpRequest):
    
    def index(request):
        alumno = FormularioAlumno()
        return render(request, 'curso/AlumnoIndex.html', {'form': alumno})
    

    def procesar_formulario(request):
        alumno = FormularioAlumno(request.POST)
        
        if alumno.is_valid():
            alumno.save()
            alumno = FormularioAlumno()
        
        return render(request, 'curso/AlumnoIndex.html', {'form': alumno, 'mensaje':'alumno registrado'})
    
    
    def listar_alumnos(request):
        alumnos = Alumno.objects.all()
        return render(request, 'curso/listaAlumnos.html', {'alumnos': alumnos})
    
    
    def edit(request, id_alumno):
        alumno = Alumno.objects.filter(id=id_alumno).first()
        form = FormularioAlumno(instance=alumno)
        return render(request, 'curso/AlumnoEdit.html', {'form': form, 'alumno': alumno})
        
    
    def actualizar(request, id_alumno):
        alumno = Alumno.objects.get(pk=id_alumno)
        form = FormularioAlumno(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
        alumnos = Alumno.objects.all()
        return render(request, 'curso/listaAlumnos.html', {'alumnos': alumnos})
    
    
    def delete(request, id_alumno):
        alumno = Alumno.objects.get(pk = id_alumno)
        alumno.delete()
        alumnos = Alumno.objects.all()
        return render(request, 'curso/ListaAlumnos.html', {'alumnos': alumnos})        
            

    