from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('planos/', views.planos, name='planos'),
]



