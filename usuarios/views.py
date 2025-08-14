from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm  # Adicione esta importação
from django.contrib import messages

# Classe login (MANTIDO ORIGINAL - NÃO MODIFICADO)
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

# Classe planos (MANTIDO ORIGINAL - NÃO MODIFICADO)
def planos(request):
    return render(request, 'planos.html')

# --- NOVA FUNÇÃO ADICIONADA (SEM AFETAR O EXISTENTE) ---
def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga automaticamente
            messages.success(request, 'Cadastro realizado!')
            return redirect('home')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})