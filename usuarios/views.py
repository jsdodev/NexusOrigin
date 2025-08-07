from django.shortcuts import render, get_object_or_404
from .models import Usuario

def home(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

def detalhes(request, usuario_id):
    usuario = get_object_or_404(usuario, id=usuario_id)
    return render(request, 'usuarios/detalhe_usuario.html', {'usuario': usuario})
