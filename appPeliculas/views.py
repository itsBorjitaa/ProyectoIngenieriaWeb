from django.shortcuts import render, get_object_or_404, redirect
from .models import Pelicula, Director, Actor, Post
from django.http import JsonResponse
import requests
from django.contrib import messages
from .forms import FormularioSuscripcion
from itertools import groupby

# config twitter
API_KEY = 'cS8PmNBRKKXsWe4QVeqeY3lqq'
API_SECRET_KEY = '7TMv6W4CKR5pzPXxX3yohXX3CrrxRDjqe47WE9oRpRrkIbM1yh'
ACCESS_TOKEN = '1859499698463309826-7RrrRm2ajCFLgh6hPVbMgRPcQcNqqs'
ACCESS_TOKEN_SECRET = 'liDrorPAq4zeZf0HV6Z0t2vUIIzvDabhFx7Tonkgkb1VD'

def obtenerTweets(request):
        # IDs de los tweets
        tweet_ids = "1859502697163989153,1859506489985003974,1862044186872049752"
        url = f"https://api.twitter.com/2/tweets?ids={tweet_ids}"
        headers = {
                "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAAVixAEAAAAAnH8X2lhkdIkOdNU%2FEIHiEjv1LtI%3DEqB9SiPXWnaeZ2AeUF7jEElieeutYGjh4Ik1RLdzzAyS2iVDxv"
        }

        try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                tweets_data = response.json()
                return JsonResponse(tweets_data)
        except requests.exceptions.RequestException as e:
                return JsonResponse({"error": str(e)}, status=500)

def obtenerPosts(request):
        posts = Post.objects.all().values('id','titulo','contenido','fecha_publicacion')
        return JsonResponse(list(posts), safe=False)


def index(request):
        peliculas_recientes = Pelicula.objects.order_by('-fecha')[:5]  # Las 5 más recientes

        if request.method == 'POST':
                form = FormularioSuscripcion(request.POST)
                if form.is_valid():
                        form.save()
                        messages.success(request, 'Te has suscrito correctamente a nuestra newsletter.')
                        return redirect('index')  # redirige a la pagina principal una vez hecho
        else:
                form = FormularioSuscripcion()

        context = {
                'peliculas_recientes': peliculas_recientes,
                'form': form,
        }
        return render(request, 'index.html', context)

def listaPeliculas(request, genero=None):
        if genero:
                genero = genero.replace('-', ' ').strip()
                peliculas = Pelicula.objects.filter(genero__nombre__icontains=genero)
        else:
                peliculas = Pelicula.objects.all()
        
        # para agrupar y ordenar las peliculas por orden alfabetico
        peliculasAgrupadas = {}
        for key, group in groupby(peliculas, lambda p: p.titulo[0].upper()):
                peliculasAgrupadas[key] = list(group)

        return render(request, 'listaPeliculas.html', {'peliculasAgrupadas': peliculasAgrupadas, 'genero': genero})

def listaDirectores(request):
        directores = Director.objects.all().order_by('nombre')  # para ordenar alfabéticamente
        # para agrupar por la inicial del nombre
        directoresAgrupados = {}
        for key, group in groupby(directores, lambda d: d.nombre[0].upper()):
                directoresAgrupados[key] = list(group)

        return render(request, 'listaDirectores.html', {'directoresAgrupados': directoresAgrupados})

def listaActores(request):
        actores = Actor.objects.all().order_by('nombre')  # para ordenar alfabéticamente
        # para agrupar por la inicial del nombre
        actoresAgrupados = {}
        for key, group in groupby(actores, lambda a: a.nombre[0].upper()):
                actoresAgrupados[key] = list(group)

        return render(request, 'listaActores.html', {'actoresAgrupados': actoresAgrupados})

def detallePelicula(request, titulo):
        pelicula = get_object_or_404(Pelicula, titulo=titulo)
        return render(request, 'detallePelicula.html', {'pelicula': pelicula})

def detalleDirector(request, id):
        director = get_object_or_404(Director, id=id)
        return render(request, 'detalleDirector.html', {'director': director})

def detalleActor(request, id):
        actor = get_object_or_404(Actor, id=id)
        return render(request, 'detalleActor.html', {'actor': actor})