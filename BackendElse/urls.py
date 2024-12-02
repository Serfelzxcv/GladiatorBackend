# BackendElse/urls.py
from django.contrib import admin
from django.urls import path,include  
from gladiadores import views  # Importar las vistas desde la app 'gladiadores'

urlpatterns = [
    path('admin/', admin.site.urls),
     path('api/', include('gladiadores.urls')), 
    path('gladiadores/', views.GladiadorList.as_view(), name='gladiador-list'),
]
