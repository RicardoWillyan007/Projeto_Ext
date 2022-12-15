from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    matricula = models.CharField('matricula', max_length=15, unique=True)
    nome = models.CharField('nome', max_length=100)
    idade = models.IntegerField('idade')
    nascimento = models.DateField('nascimento')
    telefone = models.CharField('telefone', max_length=100)
    cpf = models.CharField('cpf', max_length=100)

    USERNAME_FIELD = 'matricula'

