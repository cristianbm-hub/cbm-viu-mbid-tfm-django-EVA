from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
# importar model Usuario
from .models import Usuario

# Create your views here.

def index(request):
    return render(request, 'helloworld.html')

def usuario(request, codigo_usuario):
    print(codigo_usuario)
    #crear objeto json
    usuario = get_object_or_404(Usuario, codigo_usuario=codigo_usuario)
 
    return JsonResponse({
            'id': usuario.id,
            'codigo_usuario': usuario.codigo_usuario,
            'nombre': usuario.nombre,
            'rango': usuario.rango,
            'fecha_nacimiento': str(usuario.fecha_nacimiento),
            'fecha_ingreso': str(usuario.fecha_ingreso),
            'unidad': usuario.unidad,
            'especialidad': usuario.especialidad,
            'grupo_sanguineo': usuario.grupo_sanguineo,
            'alergias': usuario.alergias,
            'condiciones_medicas': usuario.condiciones_medicas,
        })