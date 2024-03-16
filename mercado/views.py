from django.shortcuts import render
from mercado.models import Produtos
# Create your views here.

def home (request):

    produtos = Produtos.objects.order_by

    context = {'produtos':produtos}


    return render(request, 'index.html', context)