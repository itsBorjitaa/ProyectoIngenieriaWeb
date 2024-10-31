from django.shortcuts import render
from .models import Pelicula, Director, Actor

def index(request):
        return render(request, 'index.html')

def listaPeliculas(request):
        peliculas = Pelicula.objects.all()
        return render(request, 'listaPeliculas.html', {'peliculas': peliculas})

def listaDirectores(request):
        directores = Director.objects.all()
        return render(request, 'listaDirectores.html', {'directores': directores})

def listaActores(request):
        actores = Actor.objects.all()
        return render(request, 'listaActores.html', {'actores': actores})