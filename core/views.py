from django.shortcuts import render

def perfil(request):
    return render(request, 'perfil.html')

def home(request):
    return render(request, 'index.html')
