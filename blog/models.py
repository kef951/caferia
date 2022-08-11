from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model):
    name = models.CharField('Titutlo',max_length=100)
    created = models.DateTimeField('Fecha de creacion',auto_now_add=True)
    updated = models.DateTimeField('Fecha de modificacion',auto_now=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering=['-created']
        
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('Titutlo',max_length=100)
    content = models.TextField('Contenido')
    published = models.DateTimeField('Fecha de publicacion', default=now)
    image = models.ImageField('Imagen', upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=CASCADE)
    categories = models.ManyToManyField(Category, 'Categorias')
    created = models.DateTimeField('Fecha de creacion',auto_now_add=True)
    updated = models.DateTimeField('Fecha de modificacion',auto_now=True)
   
    class Meta():
       verbose_name = 'Entrada'
       verbose_name = 'Entradas'
       ordering = ['-created']
    
    def __str__(self):    
        return self.title
       
    