from django.db import models
from django.contrib.auth.models import User


class PedidosModels(models.Model):
    STATUS = [
        ('A', 'Aprovado'),
        ('C', 'Criado'),
        ('R', 'Reprovado'),
        ('P', 'Pendente'),
        ('E', 'Enviado'),
        ('F', 'Finalizado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    total = models.FloatField(verbose_name='Total')
    status = models.CharField(default='C', max_length=1, choices=STATUS, verbose_name='Status')

    def __str__(self):
            return (f'Pedido nº: {self.pk}')
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        indexes = [
            models.Index(fields=["usuario"], name="usuario_pedido_idx"),
        ]

class ItensPedidosModels(models.Model):
    pedido = models.ForeignKey(PedidosModels, on_delete=models.CASCADE, verbose_name='Pedidos itens')
    produto = models.CharField(max_length=255, verbose_name='Produto')
    produto_id = models.PositiveIntegerField()
    variacao = models.CharField(max_length=255, verbose_name='Variacão')
    variacao_id = models.PositiveIntegerField()
    preco = models.FloatField(verbose_name='Preço itens')
    preco_promocional = models.FloatField(default=0, verbose_name='Preço promocional')
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade')
    imagem = models.CharField(max_length=2000)

    def __str__(self):
        return (f'Item do {self.pedido}')
    
    class Meta:
        verbose_name = "Pedido item"
        verbose_name_plural = "Pedidos itens"
        indexes = [
            models.Index(fields=["produto_id"], name="pedido_id_idx"),
            models.Index(fields=["variacao_id"], name="variacao_id_idx"),
        ]

"""
Models:
    Pedido:
        user - FK User
        total - Float
        status - Choices
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),

        ItemPedido:
            pedido - FK pedido
            produto - Char
            produto_id - Int
            variacao - Char
            variacao_id - Int
            preco - Float
            preco_promocional - Float
            quantidade - Int
            imagem - Char
"""