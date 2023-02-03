from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    matricula = models.CharField('matricula', max_length=15, unique=True)
    nome = models.CharField('nome', max_length=100)
    nascimento = models.DateField('nascimento')
    telefone = models.CharField('telefone', max_length=100)
    cpf = models.CharField('cpf', max_length=11, unique=True)
    username = models.CharField(null=True, max_length=10) #Desabilitando username

    USERNAME_FIELD = 'cpf'



#Ordem de implementação dos CRUDS: Area, Projeto, Vagas


class Area(models.Model):
    nome = models.CharField('nome', max_length=100)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField('titulo', max_length=100)
    resumo = models.CharField('resumo', max_length=100)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

class Vagas(models.Model):
    descricao = models.CharField('descricao', max_length=100)
    quantidade = models.IntegerField('quantidade')
    perfil = models.CharField('perfil', max_length=100)
    ch = models.IntegerField('CH')
    data_inicio = models.DateField('data_inicio', max_length=100)
    data_fim = models.DateField('data_fim', max_length=100)
    projeto = models.ForeignKey(Projeto, on_delete=models.PROTECT)



# class Curso(models.Model):
# nome = models.CharField('nome', max_length=100)




    