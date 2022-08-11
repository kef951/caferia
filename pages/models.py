from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField("Titulo", max_length=200)
    content =  RichTextField("Contenido")
    order = models.SmallIntegerField('Orden', default=0)
    created = models.DateTimeField('Fecha de creacion',auto_now_add=True)
    updated = models.DateTimeField('Fecha de modificacion',auto_now=True)
    
    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"
        ordering = ['order','title']
        
    def __str__(self):
        return self.title