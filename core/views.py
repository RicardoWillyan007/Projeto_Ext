from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UsuarioForm, AreaForm, VagaForm
from .models import Vagas, Area

def home(request):
    return render(request, 'index.html')

@login_required
def perfil(request):
    return render(request, 'perfil.html')


#Areas
def area_cadastrar(request):
    form = AreaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar_area')
    contexto = {
        'form': form
    }
    return render(request, 'cadastrar_area.html', contexto)

def area_listar(request):
    area = Area.objects.all()
    contexto = {
        'listar_area': area
    } 
    return render(request, 'area.html', contexto)

def area_editar(request, id):
    areas = Area.objects.get(pk=id)

    form = AreaForm(request.POST or None, instance=areas)
    if form.is_valid():
        form.save()
        return redirect('listar_area')

    contexto = {
        'form': form
    }
    return render(request, 'cadastrar_area.html', contexto)

def area_remover(request, id):
    areas = Area.objects.get(pk=id)
    areas.delete() 
    return redirect('listar_area')


#Vagas
def vaga_cadastrar(request):
    form = VagaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('vagas_listar')
    contexto = {
        'form': form
    }
    return render(request, 'cadastrar_vagas.html', contexto)

def vaga_listar(request):
    vagas = Vagas.objects.all()
    contexto = {
        'listar_vagas': vagas
    } 
    return render(request, 'vaga.html', contexto)

def vaga_editar(request, id):
    vagas = Vagas.objects.get(pk=id)

    form = VagaForm(request.POST or None, instance=vagas)
    if form.is_valid():
        form.save()
        return redirect('listar_vagas')

    contexto = {
        'form': form
    }
    return render(request, 'cadastrar_vaga.html', contexto)

def vaga_remover(request, id):
    areas = Vagas.objects.get(pk=id)
    areas.delete() 
    return redirect('vagas_listar')



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

