from django import forms
from .models import Alumno

class FormularioAlumno(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = {'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})}