from django.contrib import admin
from django.urls import path
from appalumnos.views import saludo, miEdad, index, alumnos, busqueda_alumnos, save_alumno, buscar_alumnos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('edad/<int:edad>/', miEdad),
    path('', index),
    
    path('frmalumnos', alumnos),
    path('frmbusqueda_alumnos', busqueda_alumnos),
    path('alumnos', save_alumno),
    path('buscar_alumnos', buscar_alumnos),
    
   
     
]
