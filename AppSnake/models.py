from django.db import models

# Create your models here.

class Comprador(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    mail=models.EmailField()
    auto=models.IntegerField()
    oferta=models.IntegerField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido:{self.apellido} - Se busca: {self.auto} - Se ofrece hasta: {self.oferta}'
class Vendedor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    mail=models.EmailField()
    modelo=models.IntegerField()
    kilometros=models.IntegerField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Auto en venta: {self.modelo} - Kilometros: {self.kilometros}'
class Auto(models.Model):
    modelo= models.CharField(max_length=30)
    año= models.DateField()
    kilometros=models.IntegerField()
    
    def __str__(self):
        return f"Modelo: {self.modelo} - Año: {self.año} - Kilometros: {self.modelo}"