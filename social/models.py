from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField('Nombre Clave', max_length= 100, unique=True) #SlugField, Obliga a usar carecteres alfanumerios, barras o guiones. NO Permite usar espacios ni caracteres especiales
    name = models.CharField("Red social", max_length=200)
    url =  models.URLField("Enlace", max_length=200, null= True, blank= True)
    created = models.DateTimeField('Fecha de creacion',auto_now_add=True)
    updated = models.DateTimeField('Fecha de modificacion',auto_now=True)
    
    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ['-created']
        
    def __str__(self):
        return self.name