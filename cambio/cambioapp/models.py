from django.db import models

# Create your models here.
class cambios(models.Model):
    valor = models.FloatField()
    criado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)
    def __str__(self): 
        return str(self.valor)
    class Meta:
            ordering = ['valor']
