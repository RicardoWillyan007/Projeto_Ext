from django.shortcuts import render

def perfil_user(request):
    return render(request, 'perfil.html')

def home(request):
    return render(request, 'index.html')
