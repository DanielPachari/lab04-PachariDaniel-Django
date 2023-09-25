from django.urls import path
from . import views

urlpatterns = [
    path('entradas/', views.lista_entradas, name='lista_entradas'),
    path('autor/<str:nombre_autor>/', views.entradas_por_autor, name='entradas_por_autor'),
    path('autores/', views.lista_autores, name='lista_autores'),
    
]

