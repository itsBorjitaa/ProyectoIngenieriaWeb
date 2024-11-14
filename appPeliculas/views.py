from django.shortcuts import render, get_object_or_404
from .models import Pelicula, Director, Actor

def index(request):
        peliculas_destacadas = Pelicula.objects.order_by('-fecha')[:5]  #las 5 más recientes
        return render(request, 'pruebaPlantilla.html', {'peliculas_destacadas': peliculas_destacadas})

def listaPeliculas(request):
        peliculas = Pelicula.objects.all()
        return render(request, 'listaPeliculas.html', {'peliculas': peliculas})

def listaDirectores(request):
        directores = Director.objects.all()
        return render(request, 'listaDirectores.html', {'directores': directores})

def listaActores(request):
        actores = Actor.objects.all()
        return render(request, 'listaActores.html', {'actores': actores})

def detallePelicula(request, titulo):
        pelicula = get_object_or_404(Pelicula, titulo=titulo)
        return render(request, 'detallePelicula.html', {'pelicula': pelicula})

def detalleDirector(request, id):
        director = get_object_or_404(Director, id=id)
        return render(request, 'detalleDirector.html', {'director': director})

def detalleActor(request, id):
        actor = get_object_or_404(Actor, id=id)
        return render(request, 'detalleActor.html', {'actor': actor})