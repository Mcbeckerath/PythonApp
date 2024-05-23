from typing import Any, Mapping
from django import forms
from django.contrib.auth.models import User, Group
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
        fields = ['username', 'first_name','cpf','email','password','tipo_usuario'] 
        labels = {
            'username': 'Usuario',
            'first_name': 'Nome',
            'cpf': 'CPF ou CNPJ',
            'email': 'Email',
            'password' : 'Senha',
            'tipo_usuario' : 'Tipo de usuário'
        }       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Usuario', 'required': 'required'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome Completo*', 'required': 'required'})
        self.fields['cpf'].widget.attrs.update({'class': 'form-control', 'placeholder': 'CPF ou CNPJ*', 'required': 'required'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email*', 'required': 'required'})    
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha*', 'required': 'required'})    
        #self.fields['telefone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Telefone*', 'required': 'required'})      
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
class UserForm (forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username','password','first_name','last_name','email','cpf','matricula','cargo','local']
        widgets = {'password': PasswordInput(),'cpf':TextInput(),'matricula':TextInput()}
    def __init__ (self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['username'].widget.attrs.update({'required':'True','placeholder':'Login','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['password'].widget.attrs.update({'required':'True','placeholder':'Senha','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['first_name'].widget.attrs.update({'required':'True','placeholder':'Nome','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['last_name'].widget.attrs.update({'required':'True','placeholder':'Sobrenome','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['email'].widget.attrs.update({'required':'True','placeholder':'Email','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['cpf'].widget.attrs.update({'required':'True','placeholder':'CPF','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['matricula'].widget.attrs.update({'required':'True','placeholder':'Matrícula','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['cargo'].widget.attrs.update({'required':'True','class':'col form-control my-2 p-2'})
        self.fields['local'].widget.attrs.update({'required':'True','class':'col form-control my-2 p-2'})