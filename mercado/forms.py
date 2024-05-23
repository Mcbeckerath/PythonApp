from typing import Any, Mapping
from django import forms
from django.contrib.auth.models import User
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.forms.widgets import *
from .models import Produtos
from .models import Usuario
from .models import Comentario


class LoginForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'password']
        widgets = {'password': PasswordInput()}
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder':'Nome de Usuário',
            'class' : 'form-control'} )
        
        self.fields['password'].widget.attrs.update(
            {'placeholder':'Senha',
             'class' : 'form-control',})    
    
       



class ProdutosForm(forms.ModelForm):
    class Meta: 
        model = Produtos
        fields = "__all__"
        labels = {
            'nome': 'Nome',
            'valor': 'Valor',
            'descricao': 'Descricao',
            'imagem': 'Imagem',
            'categoria_produto': 'Categoria do Produto',
            'estado_produto': 'Estado do Produto'           
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        self.fields['valor'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Valor*', 'required': 'required'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descricao*', 'required': 'required'})
        self.fields['imagem'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Imagem*', 'required': 'required'})
        self.fields['categoria_produto'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Categoria do Produto*', 'required': 'required'})
        self.fields['estado_produto'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Estado do Produto*', 'required': 'required'})

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = "__all__" 
        labels = {
            'nome': 'Nome',
            'CPF_CNPJ': 'CPF ou CNPJ',
            'email': 'Email',
            'senha' : 'Senha',
            'telefone' : 'Telefone',
            'tipo_usuario' : 'Tipo de usuário'
        }       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome Completo*', 'required': 'required'})
        self.fields['CPF_CNPJ'].widget.attrs.update({'class': 'form-control', 'placeholder': 'CPF ou CNPJ*', 'required': 'required'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email*', 'required': 'required'})    
        self.fields['senha'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha*', 'required': 'required'})    
        self.fields['telefone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Telefone*', 'required': 'required'})      
        self.fields['tipo_usuario'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tipo de Usuário*', 'required': 'required'})    
  


class ComentarioForm(forms.ModelForm):
    class Meta: 
        model = Comentario
        fields = "__all__"
        labels = {
            'texto': 'Texto',
            'avaliacao': 'Avaliação',
            'usuario': 'Usuário',
            'produto': 'Produto',        
            }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['texto'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Texto*', 'required': 'required'})
        self.fields['avaliacao'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Avliação*', 'required': 'required'})
        self.fields['usuario'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Usuário*', 'required': 'required'})    
        self.fields['produto'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Produto*', 'required': 'required'})            
#comentario