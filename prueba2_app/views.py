
from django.shortcuts import render, get_object_or_404, redirect
from .models import Socio
from .forms import SocioForm

def listar_socios(request):
    socios = Socio.objects.all()
    return render(request, 'listar_socios.html', {'socios': socios})

def agregar_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_socios')
    else:
        form = SocioForm()

    return render(request, 'agregar_socio.html', {'form': form})

def modificar_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    if request.method == 'POST':
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect('listar_socios')
    else:
        form = SocioForm(instance=socio)
    return render(request, 'modificar_socio.html', {'form': form, 'socio': socio})

def eliminar_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    socio.delete()
    return redirect('listar_socios')
    
def user_view(request):
    nombre = "Benjamin Muñoz Pelizari Tomas"
    edad = 20
    correo = "benjamin.munoz59@inacapmail.cl"
    carrera = "Ingenieria Informatica"

    return render(request, 'user.html', {'nombre': nombre, 'edad': edad, 'correo': correo, 'carrera': carrera})
    
def index(request):
    return render(request, 'index.html')
