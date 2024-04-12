from django import forms
from mercado.models import Produtos

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fiels =['nome, valor, categoria, descricao, imagem, estado_produto']
        

