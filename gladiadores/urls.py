# gladiadores/urls.py
from django.urls import path
from .views import GladiadorList, GladiadorDetail

urlpatterns = [
    path('gladiadores/', GladiadorList.as_view(), name='gladiador-list'),
    path('gladiadores/<int:pk>/', GladiadorDetail.as_view(), name='gladiador-detail'),
]
