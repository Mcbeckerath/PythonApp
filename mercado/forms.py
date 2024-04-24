from django import forms 
from .models import Produtos


class ProdutosForm(forms.ModelForm):
    class Meta: 
        model = Produtos
        fields = ['nome', 'valor', 'descricao', 'imagem', 'categoria_produto', 'estado_produto']
        labels = {
            'nome': 'Nome',
            'valor': 'Valor',
            'descricao': 'Descricao',
            'imagem': 'Imagem',
            'categoria_produto': 'Categoria do Produto',
            'estado_produto': 'Estado do Produto'           
            }
        