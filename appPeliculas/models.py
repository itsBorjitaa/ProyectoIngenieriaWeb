from django.db import models

class Director(models.Model):
    #campos
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    url_imagen = models.URLField(blank=True, null=True)

    #metadata
    class Meta:
        ordering = ["nombre"]

    #metodos
    def __str__(self):
        return self.nombre
    

class Actor(models.Model):
    #campos
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    url_imagen = models.URLField(blank=True, null=True)

    #metadata
    class Meta:
        ordering = ["nombre"]

    #metodos
    def __str__(self):
        return self.nombre
    

class Pelicula(models.Model):
    #campos
    titulo = models.CharField(max_length=120)
    año = models.DateField()
    url_imagen = models.URLField(blank=True, null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actores = models.ManyToManyField(Actor)

    #metadata
    class Meta:
        ordering = ["titulo"]

    #metodos
    def __str__(self):
        return self.titulo
    
