from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Produtos (models.Model):

    nome = models.CharField(max_length=250)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=1500)
    imagem = models.CharField(max_length=250)
    categoria_produto = models.ForeignKey("Categoria_Produto",on_delete=models.CASCADE, null=True)
    estado_produto = models.ForeignKey("Estado_Produto", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nome
    
class Categoria_Produto (models.Model):
     nome = models.CharField(max_length=250)
     def __str__(self):
        return self.nome
     
class Estado_Produto (models.Model):
    nome = models.CharField(max_length=250)
    def __str__(self):
        return self.nome   
    
class Usuario (User):
            
    CPF_CNPJ = models.CharField(max_length=250)
    telefone = models.CharField(max_length=250)
    tipo_usuario = models.ForeignKey("Tipo_Usuario", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.CPF_CNPJ


class Tipo_Usuario (models.Model):
    nome = models.CharField(max_length=250)
    def __str__(self):
        return self.nome  

class Comentario(models.Model):
    texto = models.CharField(max_length=250)
    avaliacao = models.DecimalField(max_digits=5, decimal_places=1)
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE, null=True)
    produto = models.ForeignKey("Produtos", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.texto   

class Pedido(models.Model):
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE, null=True)
    produto = models.ForeignKey("Produtos", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.usuario 

class Pagamento(models.Model):
    tipo =  models.CharField(max_length=250)
    total_preco = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    pedido = models.ForeignKey("Pedido",on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.tipo 


