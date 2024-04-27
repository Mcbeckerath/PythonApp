from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from mercado.models import Produtos
from mercado.forms import  ProdutosForm, UsuarioForm, LoginForm, ComentarioForm
from django.contrib.auth import login as authLogin, authenticate, logout

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
    form = ProdutosForm()
   
    if request.method == 'POST':
            form = ProdutosForm(request.POST)

            if form.is_valid():
                form.save()
                form = ProdutosForm()  

    context = {'form': form}
    return render (request, 'formulario_produto.html', context)

def form_usuario(request):

    """Adiciona um novo produto"""
    form = UsuarioForm()
   
    if request.method == 'POST':
            form = UsuarioForm(request.POST)

            if form.is_valid():
                form.save()
                form = UsuarioForm()  

    context = {'form': form}    
    return render (request, 'formulario_usuario.html', context)

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  
        user = authenticate(username=username, password=password)

        if user:  
            authLogin(request, user)
            return HttpResponseRedirect(reverse('home')) 
        
    form  = LoginForm()
    context = {'form': form}
    return render (request, 'base.html', context)         

def logout_view(request):

    logout(request)
    return HttpResponseRedirect(reverse('home')) 

def form_comentario(request):
    form = ComentarioForm()
   
    if request.method == 'POST':
            form = ComentarioForm(request.POST)

            if form.is_valid():
                form.save()
                form = ComentarioForm()  

    context = {'form': form}    
    return render (request, 'comentario.html', context)
     