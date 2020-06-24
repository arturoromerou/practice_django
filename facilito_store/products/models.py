from django.db import models

# todo las clases que hereden models.Model sera una tabla en la bd, los atributos seran columnas en la tabla
class Product(models.Model): 
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0) # maximo 8 digitos y 2 decimales
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
