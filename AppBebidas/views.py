from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Cerveza
from .forms import nuevaCerveza
# Create your views here.
def inicio (request):
    return render(request, f'AppBebidas\inicio.html',{})

def lista_cervezas(request):
    
    cervezas = None
    if request.method == 'GET':
        busqueda_marca = request.GET.get('marca', '')
        if busqueda_marca == '':
            cervezas = Cerveza.objects.all()
        else:
            cervezas = Cerveza.objects.filter(marca=busqueda_marca)

    return render(request, f'AppBebidas\listaCerveza.html',{'unidad_cervezas': cervezas})

def lista_gaseosas(request):
    return render(request, f'AppBebidas\listaGaseosas.html',{})

def lista_vinos(request):
    return render(request, f'AppBebidas\listaVino.html',{})

def nueva_cerveza(request):
    
    if request.method == 'POST':
        formulario_cerveza= nuevaCerveza(request.POST)
        
        if formulario_cerveza.is_valid():
            
            cerveza_datos = formulario_cerveza.cleaned_data
            cerveza = Cerveza(marca=cerveza_datos['marca'],tipo=cerveza_datos['tipo'],capacidad=cerveza_datos['capacidad'])     
            cerveza.save()
            return redirect ('listaCervezas')
            
    formulario_cerveza= nuevaCerveza()
    return render(request,f'AppBebidas\crearCerveza.html',{'formulario_cerveza': formulario_cerveza})