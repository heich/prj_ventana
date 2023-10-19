from django.urls import path
from . import views

urlpatterns = [path('', views.registro, name='registro')]


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/', views.registro, name='registro'),
    path('seleccion-adjetivos/', views.seleccion_adjetivos, name='seleccion_adjetivos'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    # Otras rutas necesarias...
]
