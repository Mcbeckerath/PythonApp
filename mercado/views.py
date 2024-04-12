from django.shortcuts import render
from mercado.models import Produtos
from mercado.forms import ProdutoForm
# Create your views here.

def home (request):

    produtos = Produtos.objects.order_by

    context = {'produtos':produtos}


    return render(request, 'index.html', context)

def produto (request,id_produto):

    produto = Produtos.objects.get(id=id_produto)
                                   
    context = {'produto':produto}

    forms = ProdutoForm()
    context2 = {'form': forms}
    
    return render(request, 'produto.html', context, context2)

      
