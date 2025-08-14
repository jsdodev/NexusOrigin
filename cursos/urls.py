# cursos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # URL da sua página inicial
    path('', views.home, name='home'),

    # URL para a página de detalhes de um curso
    # O <str:slug> captura o nome do curso na URL (ex: /cursos/ia/)
    path('cursos/<str:slug>/', views.curso_detalhes, name='curso_detalhes'),

    # URL da sua API para pegar os dados de um curso (se você for usar)
    path('api/curso/<str:slug>/', views.api_curso, name='api_curso'),
]