from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from mercado.models import Produtos
from .forms import  ProdutosForm
# Create your views here.

def home (request):

    produtos = Produtos.objects.order_by

    context = {'produtos':produtos}

    return render(request, 'index.html', context)


def produto (request,id_produto):

    produto = Produtos.objects.get(id=id_produto)
                                   
    context = {'produto':produto}

    return render(request, 'produto.html', context)

      
def contato (request):

    return render(request, 'contato.html')


def sobre (request):

    return render(request, 'sobre.html')


def form_produto(request):
    """Adiciona um novo produto"""
    if request.method != 'POST':
        #Nenhum dado submetido; cria um formulario em branco
        form = ProdutosForm()
    else:
        #Dados de POST submetidos; processa dados
        form = ProdutosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produto'))


    context = {'form': form}
    return render (request, 'mercado/form_produto.html', context)
