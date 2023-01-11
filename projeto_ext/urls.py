"""projeto_ext URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, perfil, autenticacao, desconectar, registro
from django.conf import settings
from django.conf.urls.static import static
from core.views import area_cadastrar, area_editar, area_listar, area_remover 
from core.views import vaga_cadastrar, vaga_listar, vaga_editar, vaga_remover

urlpatterns = [
    path('login/', autenticacao, name='login'),
    path('logout/', desconectar, name='logout'),
    path('', home, name='home'),
    path('perfil/', perfil, name='perfil'),
    path('registro/', registro, name='registro'),
    path('admin/', admin.site.urls),


    path('add_area/', area_cadastrar, name='cadastrar_area'),
    path('listar_area/', area_listar, name='cadastrar_area'),
    path('editar_area/<int:id>/', area_editar, name='cadastrar_area'),
    path('remover_area/<int:id>/', area_remover, name='cadastrar_area'),


    path('add_vaga/', vaga_cadastrar, name='cadastrar_vaga'),
    path('listar_vaga/', vaga_listar, name='cadastrar_vaga'),
    path('editar_vaga/<int:id>/', vaga_editar, name='cadastrar_vaga'),
    path('remover_vaga/<int:id>/', vaga_remover, name='cadastrar_vaga'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
