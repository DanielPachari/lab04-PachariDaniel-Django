from django.shortcuts import render
from .models import Autor, Entrada
from django.shortcuts import render, get_object_or_404

def lista_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'blog/lista_entradas.html', {'entradas': entradas})

def entradas_por_autor(request, nombre_autor):
    autor = get_object_or_404(Autor, nombre=nombre_autor)
    entradas = Entrada.objects.filter(autor=autor)
    return render(request, 'blog/entradas_por_autor.html', {'autor': autor, 'entradas': entradas})

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'blog/lista_autores.html', {'autores': autores})
