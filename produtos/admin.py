from django.contrib import admin
from .models import ProdutosModels, VariacaoProdutosModel


# incluindo models de variação junto com o model Produto
class VariacaoInline(admin.TabularInline):
    model = VariacaoProdutosModel
    extra = 1

# incluindo no models admin produtos
class ProdutosInlineAdmin(admin.ModelAdmin):
    inlines = [
        VariacaoInline
    ]

admin.site.register(ProdutosModels, ProdutosInlineAdmin)
admin.site.register(VariacaoProdutosModel)
