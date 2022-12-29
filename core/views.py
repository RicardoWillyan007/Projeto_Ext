from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UsuarioForm
from .models import Usuario

def home(request):
    return render(request, 'index.html')

@login_required
def perfil(request):
    return render(request, 'perfil.html')



#listar editar e remover NÃO PRONTO
def listar_usuario(request):
    usuarios = Usuario.objects.all()
    contexto = {
        'todos_usuarios': usuarios
    }
    return render(request, 'cursos.html', contexto)

def editar_usuario(request, id):
    usuario = Usuario.objects.get(pk=id)
    form = UsuarioForm(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return redirect('listar_usuario')

    contexto = {
        'form_usuario': form
    }

    return render(request, 'curso_cadastrar.html', contexto)  

def remover_usuario(request, id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()
    return redirect('listar_usuarios')







def autenticacao(request):
    if request.POST:
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('perfil')
        else:
            return render(request, 'registration\login.html')
    else:
        return render(request, 'registration\login.html')

def desconectar(request):
    logout(request)
    return redirect('home')

def registro(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    contexto = {
        'form': form
    }
    return render(request, 'registro.html', contexto)

