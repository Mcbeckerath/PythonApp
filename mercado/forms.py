from django import forms
from .models import Produtos
from .models import Usuario

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
            'estado' : 'Estado',
            'cidade' : ' Cidade',
            'bairro' : 'Bairro', 
            'cep' : 'CEP', 
            'endereco' : 'Endereço',  
            'numero' : 'Número', 
            'tipo_usuario' : 'Tipo de usuário'
        }       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome Completo*', 'required': 'required'})
        self.fields['CPF_CNPJ'].widget.attrs.update({'class': 'form-control', 'placeholder': 'CPF ou CNPJ*', 'required': 'required'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email*', 'required': 'required'})    
        self.fields['senha'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha*', 'required': 'required'})    
        self.fields['telefone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Telefone*', 'required': 'required'})    
        self.fields['cidade'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Cidade*', 'required': 'required'})
        self.fields['estado'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Estado*', 'required': 'required'})
        self.fields['bairro'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Bairro*', 'required': 'required'})
        self.fields['cep'].widget.attrs.update({'class': 'form-control', 'placeholder': 'CEP*', 'required': 'required'})    
        self.fields['endereco'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Endereço*', 'required': 'required'})
        self.fields['numero'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Número*', 'required': 'required'})    
        self.fields['tipo_usuario'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tipo de Usuário*', 'required': 'required'})    
  