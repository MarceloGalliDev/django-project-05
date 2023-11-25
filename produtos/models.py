
"""models for products"""
from django.db import models


class ProdutosModels(models.Model):
    codigo = models.IntegerField(primary_key=True, verbose_name="Código")
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name="Nome")
    descricao_curta = models.TextField(max_length=255, blank=False, null=False, verbose_name="Descrição curta")
    descricao_longa = models.TextField(max_length=255, blank=False, null=False, verbose_name="Descrição longa")
    imagem = models.ImageField(upload_to="produto_imagem/%Y/%m/", blank=True, null=True, verbose_name="Imagem")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    preco_marketing = models.FloatField(verbose_name="Preço marketing")
    preco_marketing_promocional = models.FloatField(verbose_name="Preço marketing promocional")
    tipo = models.CharField(
        max_length=2,
        blank=False,
        null=False,
        default='KG',
        choices=(
            ('KG', 'Kilo'),
            ('UN', 'Unidade'),
            ('PC', 'Pacote'),
            ('DY', 'Display'),
            ('FD', 'Fardo'),
        ),
        verbose_name="Tipo"
    )
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        indexes = [
            models.Index(fields=["codigo"], name="codigo_produto_idx"),
        ]

"""
Produto:
    Produto:
        nome - Char
        descricao_curta - Text
        descricao_longa - Text
        imagem - Image
        slug - Slug
        preco_marketing - Float
        preco_marketing_promocional - Float
        tipo - Choices
            ('V', 'Variável'),
            ('S', 'Simples'),

    Variacao:
        nome - char
        produto - FK Produto
        preco - Float
        preco_promocional - Float
        estoque - Int
"""