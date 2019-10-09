from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete
class tipo_proyecto(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class curso(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class imagen(models.Model):
    image = models.ImageField(upload_to="projects",blank=True)

    def __str__(self):
        return str(self.id)


class Proyecto(models.Model):
    """Model definition for Producto."""
    image = models.ImageField(upload_to="projects")
    nombre= models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.ForeignKey(tipo_proyecto,on_delete=models.PROTECT)
    curso = models.ForeignKey(curso,on_delete=models.PROTECT)
    descripcion = models.TextField(blank=True)
    tiempo = models.CharField(max_length=50,blank=True)
    Grupo = models.TextField(blank=True)
    Completo = models.BooleanField(blank=True)
    imagen = models.ManyToManyField(imagen)
    class Meta:
        """Meta definition for Producto."""

        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return u'/tienda/%d' % self.id 
