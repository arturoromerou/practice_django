from django.shortcuts import render # con esta clase renderizamos los templates.
from django.shortcuts import redirect # con esta clase redireccionamos a un url.

from django.contrib import messages # con esta clase podemos mostrar mensajes.
from django.contrib.auth import login # con esta clase podemos ingresar.
from django.contrib.auth import logout # con esta clase podemos salir de la sesion.
from django.contrib.auth import authenticate # con esta clase autenticamos los usuarios.

from django.contrib.auth.models import User # con esta clase podemos dar de alta nuevos usuarios.

from .forms import RegisterForm

from products.models import Product

def index(request):

    products = Product.objects.all().order_by('-id')

    return render(request, 'index.html', {
        # context: con este diccionario podemos pasarle valores a nuestro template
        'message': 'Listado de productos',
        'title': 'Productos',
        'products': products,
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username') # diccionario
        password = request.POST.get('password') # None

        user = authenticate(username=username, password=password) # None
        
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o Contrasenia no validos')

    return render(request, 'users/login.html', {

    })

def logout_view(request):
    logout(request)
    messages.success(request, 'sesion cerrada')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)

    # obtener informacion del formulario mediante una clase
    if request.method == 'POST' and form.is_valid(): # is_valid se encarga de validar cada campo
        

        # esto nos va a retornar un objeto del tipo user (nos permite crear nuevos usuarios)
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'creado exitosamente')
            return redirect('index')
    
    return render(request, 'users/register.html', {
        'form': form
    })