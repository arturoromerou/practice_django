import uuid

from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

# todo las clases que hereden models.Model sera una tabla en la bd, los atributos seran columnas en la tabla
class Product(models.Model): 
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0) # maximo 8 digitos y 2 decimales
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='products/', null=False, blank=False)
    created_ad = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

def set_slug(sender, instance, *args, **kwargs): #callback se va a encargar de generar un slug
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:8])
            )

        instance.slug = slug

pre_save.connect(set_slug, sender=Product)
