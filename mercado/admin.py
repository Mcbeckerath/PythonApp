from django.contrib import admin
from mercado.models import Produtos
from mercado.models import Estado_Produto
from mercado.models import Usuario
from mercado.models import Tipo_Usuario
from mercado.models import Categoria_Produto
from mercado.models import Comentario
from mercado.models import Pedido
from mercado.models import Pagamento
from mercado.models import *


# Register your models here.

admin.site.register(Produtos)
admin.site.register(Estado_Produto)
admin.site.register(Usuario)
admin.site.register(Tipo_Usuario)
admin.site.register(Categoria_Produto)
admin.site.register(Comentario)
admin.site.register(Pedido)
admin.site.register(Pagamento)
admin.site.register(Cargo)
admin.site.register(Local)
admin.site.register(Chamada)

