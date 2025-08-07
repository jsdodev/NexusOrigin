from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_usuarios'),
    path('<int:usuario_id>/', views.detalhes, name='detalhes_usuario'),
]
