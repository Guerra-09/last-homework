from django.db import models

# Create your models here.
class Resena(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    valoracion = models.IntegerField()
    photo = models.ImageField(upload_to='books', null=True, blank=True)

    def __str__(self):
        return self.nombre