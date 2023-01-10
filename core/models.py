from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    username = models.CharField('matricula', max_length=15, unique=True)
    nome = models.CharField('nome', max_length=100)
    nascimento = models.DateField('nascimento')
    telefone = models.CharField('telefone', max_length=100)
    cpf = models.CharField('cpf', max_length=100)

    USERNAME_FIELD = 'username'

class Vagas(AbstractUser):
    id = models.IntegerField('id', max_length=15, unique=True)
    descricao = models.CharField('descricao', max_length=100)
    quantidade = models.IntegerField('quantidade', max_length=100)
    perfil = models.CharField('perfil', max_length=100)
    CH = models.IntegerField('CH', max_length=100)
    data_inicio = models.DateField('data_inicio' max_length=100)
    data_fim = models.DateField('data_fim', max_length=100)

class Area(AbstractUser):
    id = models.IntegerField('id', max_length=15, unique=True)
    nome = models.CharField('nome', max_length=100)

class Curso(AbstractUser):
    id = models.IntegerField('id', max_length=15, unique=True)
    nome = models.CharField('nome', max_length=100)

class Projeto(AbstractUser):
     id = models.IntegerField('id', max_length=15, unique=True)
     titulo = models.CharField('titulo', max_length=100)
     resumo = models.CharField('resumo', max_length=100)
     responsavel = models.CharField('responsavel', max_length=100)
     vagas = models.IntegerField('vagas', max_length=100)