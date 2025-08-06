from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_cursos'),
    path('detalhes/', views.detalhes, name='detalhes_cursos'),
]
