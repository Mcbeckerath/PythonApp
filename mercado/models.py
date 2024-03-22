from django.db import models

# Create your models here.
class Produtos (models.Model):

    nome = models.CharField(max_length=250)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=250)
    descricao = models.CharField(max_length=250)
    imagem = models.CharField(max_length=250)
    estado_produto = models.ForeignKey("Estado_Produto", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nome

class Estado_Produto (models.Model):

    nome = models.CharField(max_length=250)

    def __str__(self):
        return self.nome