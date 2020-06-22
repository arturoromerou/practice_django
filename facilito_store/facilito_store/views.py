from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {
        # context: con este diccionario podemos pasarle valores a nuestro template
        'message': 'Listado de productos',
        'title': 'Productos',
        'products': [
            {'title': 'Polo', 'price': '$5', 'stock': True}, # producto
            {'title': 'Camisa', 'price': '$7', 'stock': True},
            {'title': 'Mochila', 'price': '$20', 'stock': False},
            {'title': 'Laptop', 'price': '$500', 'stock': True}
        ]
    })
