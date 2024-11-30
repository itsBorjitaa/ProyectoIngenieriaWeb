from django.apps import AppConfig


class AppPeliculasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appPeliculas'
    def ready(self): 
        import appPeliculas.signals #importa y registra los signals, los signals estarán activos sin necesidad de modificar otros archivos como models.py o views.py
