from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField('Titutlo',max_length=200,)
    subtitle = models.CharField('Subtitulo',max_length=200,)
    content = models.TextField('Contenido',max_length=200,)
    image = models.ImageField('Imagen', upload_to="servicies")
    created = models.DateTimeField('Fecha de creacion',auto_now_add=True)
    updated = models.DateTimeField('Fecha de modificacion',auto_now=True)
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering=['-created']
        
    def __str__(self):
        return self.title