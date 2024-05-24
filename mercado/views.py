from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from mercado.models import Produtos
from mercado.forms import  ProdutosForm, UsuarioForm, LoginForm, ComentarioForm
from django.contrib.auth import login as authLogin, authenticate, logout
from django.shortcuts import render
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from mercado.forms import UserForm
from django.contrib.auth.hashers import make_password
from mercado.models import Usuario
from django.contrib.auth.models import User, Permission, Group

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
                post = form.save(commit=False)
                post.password = make_password(post.password)
                post.save()
                
                return HttpResponseRedirect(reverse('login'))
                 

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
     
def encerrar (request):
    usuario = Usuario.objects.get(user_ptr_id=request.user.id)
    usuario.is_active=False
    usuario.save()
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))

def editarperfil (request):
    if request.method == 'POST':
        usuario = Usuario.objects.get(user_ptr_id=request.user.id)
        novo_usuario = request.POST.copy()
        novo_usuario['username'] = usuario.username
        novo_usuario['password'] = usuario.password
        form = UserForm(instance=usuario, data=novo_usuario)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse('index'))

'''
    Funções de superusuario
'''

def caduser (request):
    if request.method == 'POST' and request.user.is_authenticated and request.user.is_superuser:
        user = UserForm(request.POST, auto_id=False)
        if user.is_valid():
            if user.data.get('password') != user.data.get('confirmacao'):
                user.add_error('password','A senha e confirmação devem ser iguais')
            else:
                permlist = []
                for permissao in request.POST.getlist("permissao"):
                    permlist.append(Permission.objects.get(id=permissao))

                user = user.save(commit=False)
                user.password = make_password(user.password)
                user.save()

                user.user_permissions.set(permlist)
        return HttpResponseRedirect(reverse('painel'))
    return HttpResponseRedirect(reverse('index'))

def toggleactive (request,id):
    if request.method == 'GET' and request.user.is_superuser:
        usuario = Usuario.objects.get(user_ptr_id=id)
        usuario.is_active = not usuario.is_active
        usuario.save()
        return HttpResponseRedirect(reverse('painel'))
    return HttpResponseRedirect(reverse('index'))

def painel (request):
    if request.method == 'GET' and request.user.is_authenticated and request.user.is_superuser:
        permissoes = Permission.objects.order_by('id')
        permissoes_agrupadas = {}
        for permissao in permissoes:
            objeto = permissao.codename.split("_")
            if objeto[1] not in permissoes_agrupadas:
                permissoes_agrupadas[objeto[1]] = {permissao.name: permissao.id}
            else:
                permissoes_agrupadas[objeto[1]][permissao.name] = permissao.id
        contexto = {
            'formuser': UserForm(auto_id=False),
            'permissoes': permissoes_agrupadas,
            'grupos': Group.objects.all(),
            'users': [(user.id, user, UserForm(instance=user, auto_id=False)) for user in Usuario.objects.order_by('first_name')]
        }
       
        return render(request,'painel.html',contexto)
    return HttpResponseRedirect(reverse('home'))

def edituser(resquest, id):
    if resquest.method == 'POST' and resquest.user.is_authenticated and resquest.user.is_superuser:
        usuario = Usuario.objects.get(user_ptr_id=id)
        novo_usuario =resquest.Post.copy()
        novo_usuario['password']=usuario.password
        form = UserForm(instance=usuario, data=novo_usuario, auto_id=False)
        if form.is_valid():
            user = form.save()
            permlist = []
            for permissao in resquest.Post.getlist("permissão"):
                permlist.append(Permission.objects.get(id=permissao))
            user.user_permissions.set(permlist)
        return HttpResponseRedirect(reverse('painel'))
    return HttpResponseRedirect(reverse('index')) 