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

from core.views import editar_usuario, remover_usuario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', autenticacao, name='login'),
    path('logout/', desconectar, name='logout'),
    path('', home, name='home'),
    path('perfil/', perfil, name='perfil'),
    path('registro/', registro, name='registro'),
    path('admin/', admin.site.urls),

    path('curso_editar/<int:id>/', editar_usuario, name='editar_usuario'),
    path('curso_remover/<int:id>/', remover_usuario, name='remover_usuario'),
]
