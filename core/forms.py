from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Vagas, Area
from django.forms import ModelForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['matricula', 'password1', 'password2', 'email', 'nome',
         'cpf', 'telefone', 'nascimento']

class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = ['id', 'nome']

class VagaForm(ModelForm):
    class Meta:
        model = Vagas
        fields = ['id', 'descricao', 'quantidade', 'perfil', 'ch', 'data_inicio', 'data_fim']
