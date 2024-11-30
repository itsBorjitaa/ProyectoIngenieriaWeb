from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Post, Suscriptor

@receiver(post_save, sender=Post)
def enviar_correo_a_suscriptores(sender, instance, created, **kwargs): #kwargs permite aceptar una cantidad variable de argumentos clave-valor (keyword arguments)
    if created:
        suscriptores = Suscriptor.objects.values_list('email', flat=True)
        lista_correos = list(suscriptores)

        # detalles
        asunto = f"Nuevo post en SanmiFlix: {instance.titulo}"
        mensaje = f"Hola, se ha publicado un nuevo post en SanmiFlix:\n\nTítulo: {instance.titulo}\n\nContenido: {instance.contenido}\n\n¡No te lo pierdas!"
        remitente = 'sanmiflix.contact@gmail.com'

        send_mail(asunto, mensaje, remitente, lista_correos)
