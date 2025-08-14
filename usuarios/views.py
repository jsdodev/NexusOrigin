from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
#classe login
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Campo do formulário
        password = request.POST.get('password')  # Campo do formulário
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após o login
        else:
            messages.error(request, 'E-mail ou senha inválidos.')
    
    return render(request, 'login.html')  # Renderiza o template de login
#Classe planos
def planos(request):
    
    return render(request, 'planos.html')