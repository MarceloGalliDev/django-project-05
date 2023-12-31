
"""models for products"""
from django.db import models
from PIL import Image
import os
from django.conf import settings
# biblioteca para gerar slug unique
from django.utils.text import slugify


class ProdutosModels(models.Model):
    codigo = models.IntegerField(primary_key=True, verbose_name="Código")
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name="Nome")
    descricao_curta = models.TextField(max_length=255, blank=False, null=False, verbose_name="Descrição curta")
    descricao_longa = models.TextField(max_length=2000, blank=False, null=False, verbose_name="Descrição longa")
    imagem = models.ImageField(upload_to="produto_imagem/%Y/%m/", blank=True, null=True, verbose_name="Imagem")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="Slug")
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


    @staticmethod
    def resize_img(img, new_width=800):
        image_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(image_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        # regra de três para pegar a largura da imagem redimensionada
        new_height = round((new_width * original_height) / original_width)
        
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            image_full_path,
            optimize=True,
            quality=50,
        )


    def preco_formatado(self):
        return f'R$ {self.preco_marketing:.2f}'.replace(".", ",")
    preco_formatado.short_description = 'Preço'


    def preco_formatado_promo(self):
        return f'R$ {self.preco_marketing_promocional:.2f}'.replace(".", ",")
    preco_formatado_promo.short_description = 'Preço Promo'


    # subscrevendo metodo save()
    def save(self, *args, **kwargs):
              
        # criando slug com o nome e caracteres randomized
        if not self.slug:
            slug = f'{slugify(self.nome)}-{self.codigo}'
            # 
            self.slug = slug
        
        super().save(*args, **kwargs)
        
        max_size_img = 800
        
        if self.imagem:
            self.resize_img(self.imagem, max_size_img)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        indexes = [
            models.Index(fields=["codigo"], name="codigo_produto_idx"),
        ]


class VariacaoProdutosModel(models.Model):
    codigo = models.IntegerField(primary_key=True, verbose_name='Código variação')
    produto = models.ForeignKey(ProdutosModels, on_delete=models.CASCADE, verbose_name='Produto variação')
    nome = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nome variação')
    preco = models.FloatField(verbose_name='Preço variação')
    preco_promocional = models.FloatField(default=0, verbose_name='Preço promocional variação')
    estoque = models.PositiveIntegerField(default=1, verbose_name='Estoque')
    
    def __str__(self):
        return self.nome or self.produto.nome
    
    class Meta:
        verbose_name = "Produto variação"
        verbose_name_plural = "Produtos variações"
        indexes = [
            models.Index(fields=["codigo"], name="codigo_produto_variacao_idx"),
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