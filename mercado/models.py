from django.db import models

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
    
class Usuario (models.Model):
        
    nome = models.CharField(max_length=250)
    CPF_CNPJ = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)
    Senha = models.CharField(max_length=250)
    Telefone = models.CharField(max_length=250)
    cidade = models.ForeignKey("Cidade", on_delete=models.CASCADE, null=True)
    estado = models.ForeignKey("Estado", on_delete=models.CASCADE, null=True)
    bairro = models.ForeignKey("Bairro", on_delete=models.CASCADE, null=True)
    cep = models.ForeignKey("Cep", on_delete=models.CASCADE, null=True)
    endereco = models.ForeignKey("Endereco", on_delete=models.CASCADE, null= True)
    tipo_usuario = models.ForeignKey("Tipo_Usuario", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nome

class Cidade(models.Model):
    cidade = models.CharField(max_length=50)
    def __str__(self):
        return self.cidade

class Estado(models.Model):
    estado = models.CharField(max_length=50)
    def __str__(self):
        return self.estado

class Bairro(models.Model):
    bairro = models.CharField(max_length=250)
    def __str__(self):
        return self.bairro
class Cep(models.Model):
    cep = models.CharField(max_length=10)
    def __str__(self):
        return self.cep

class Endereco(models.Model):
    endereco = models.CharField(max_length=250)
    def __Str__(self):
        return self.endereco
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
    pedido = models.ForeignKey("Pedido",on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.tipo 


