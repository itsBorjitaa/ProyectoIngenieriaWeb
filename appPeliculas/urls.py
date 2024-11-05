from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('peliculas/', views.listaPeliculas, name='listaPeliculas'),
    path('directores/', views.listaDirectores, name='listaDirectores'),
    path('actores/', views.listaActores, name='listaActores'),
    path('peliculas/<str:titulo>/', views.detallePelicula, name='detallePelicula'),
    path('actores/<int:id>/', views.detalleActor, name='detalleActor'),
    path('directores/<int:id>/', views.detalleDirector, name='detalleDirector'),
]
