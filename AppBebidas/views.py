from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Cerveza, Gaseosa, Vino
from .forms import nuevaCerveza, nuevaGaseosa, nuevaVino
# Create your views here.
def inicio (request):
    return render(request, f'AppBebidas\inicio.html',{})

# Vistas de Cerveza
def lista_cervezas(request):
    
    cervezas = None
    if request.method == 'GET':
        busqueda_marca = request.GET.get('marca', '')
        if busqueda_marca == '':
            cervezas = Cerveza.objects.all()
        else:
            cervezas = Cerveza.objects.filter(marca=busqueda_marca)

    return render(request, f'AppBebidas\listaCerveza.html',{'unidad_cervezas': cervezas})

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

# Vista de gaseosas

def lista_gaseosas(request):
    gaseosas = None
    if request.method == 'GET':
        busqueda_marca = request.GET.get('marca', '')
        if busqueda_marca == '':
            gaseosas = Gaseosa.objects.all()
        else:
            gaseosas = Gaseosa.objects.filter(marca=busqueda_marca)

    return render(request, f'AppBebidas\listaGaseosas.html',{'unidad_gaseosas': gaseosas})

def nueva_gaseosa(request):
    
    if request.method == 'POST':
        formulario_gaseosa= nuevaGaseosa(request.POST)
        
        if formulario_gaseosa.is_valid():
            
            gaseosa_datos = formulario_gaseosa.cleaned_data
            gaseosa = Gaseosa(marca=gaseosa_datos['marca'],tipo=gaseosa_datos['tipo'],capacidad=gaseosa_datos['capacidad'],light=gaseosa_datos['light'])     
            gaseosa.save()
            return redirect ('listaGaseosas')
            
    formulario_gaseosa= nuevaGaseosa()
    return render(request,f'AppBebidas\crearGaseosa.html',{'formulario_gaseosa': formulario_gaseosa})


# Vista de Vinos

def lista_vinos(request):
    vinos = None
    if request.method == 'GET':
        busqueda_marca = request.GET.get('marca', '')
        if busqueda_marca == '':
            vinos = Vino.objects.all()
        else:
            vinos = Vino.objects.filter(marca=busqueda_marca)

    return render(request, f'AppBebidas\listaVinos.html',{'unidad_vinos': vinos})

def nueva_vino(request):
    
    if request.method == 'POST':
        formulario_vino= nuevaVino(request.POST)
        
        if formulario_vino.is_valid():
            
            vino_datos = formulario_vino.cleaned_data
            vino = Vino(marca=vino_datos['marca'],tipo=vino_datos['tipo'],capacidad=vino_datos['capacidad'])     
            vino.save()
            return redirect ('listaVinos')
            
    formulario_vino= nuevaVino()
    return render(request,f'AppBebidas\crearVino.html',{'formulario_vino': formulario_vino})