from django.contrib import admin
from .models import Actor, Director, Genero,Pelicula, Post

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(Post)