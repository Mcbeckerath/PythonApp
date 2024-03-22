from django.shortcuts import render
from mercado.models import Produtos
# Create your views here.

def home (request):

    produtos = Produtos.objects.order_by

    context = {'produtos':produtos}


    return render(request, 'index.html', context)

def produto (request,id_produto):

    produto = Produtos.objects.get(id=id_produto)
                                   
    context = {'produto':produto}

    return render(request, 'produto.html', context)

      
