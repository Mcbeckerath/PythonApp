from django.contrib import admin
from mercado.models import Produtos, Estado_Produto, Usuario, Tipo_Usuario, Categoria_Produto, Comentarios, Pedido, Pagamento
# Register your models here.

admin.site.register(Produtos)
admin.site.register(Estado_Produto)
admin.site.register(Usuario)
admin.site.register(Tipo_Usuario)
admin.site.register(Categoria_Produto)
admin.site.register(Comentarios)
admin.site.register(Pedido)
admin.site.register(Pagamento)

