from django.shortcuts import render, get_object_or_404
from .models import Pelicula, Director, Actor, Post
from django.http import JsonResponse
import requests
import time

# config twitter
API_KEY = 'cS8PmNBRKKXsWe4QVeqeY3lqq'
API_SECRET_KEY = '7TMv6W4CKR5pzPXxX3yohXX3CrrxRDjqe47WE9oRpRrkIbM1yh'
ACCESS_TOKEN = '1859499698463309826-7RrrRm2ajCFLgh6hPVbMgRPcQcNqqs'
ACCESS_TOKEN_SECRET = 'liDrorPAq4zeZf0HV6Z0t2vUIIzvDabhFx7Tonkgkb1VD'

def fetch_tweets(request):
        # IDs de los tweets
        tweet_ids = "1859502697163989153,1859506489985003974"
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
        peliculas_recientes = Pelicula.objects.order_by('-fecha')[:5]  #las 5 más recientes
        return render(request, 'index.html', {'peliculas_recientes': peliculas_recientes})

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