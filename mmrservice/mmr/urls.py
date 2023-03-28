from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_mmr, name='calculate_mmr'),
]