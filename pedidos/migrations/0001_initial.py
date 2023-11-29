# Generated by Django 4.2.7 on 2023-11-28 02:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidosModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField(verbose_name='Total')),
                ('status', models.CharField(choices=[('A', 'Aprovado'), ('C', 'Criado'), ('R', 'Reprovado'), ('P', 'Pendente'), ('E', 'Enviado'), ('F', 'Finalizado')], default='C', max_length=1, verbose_name='Status')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='ItensPedidosModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=255, verbose_name='Produto')),
                ('produto_id', models.PositiveIntegerField()),
                ('variacao', models.CharField(max_length=255, verbose_name='Variacão')),
                ('variacao_id', models.PositiveIntegerField()),
                ('preco', models.FloatField(verbose_name='Preço itens')),
                ('preco_promocional', models.FloatField(default=0, verbose_name='Preço promocional')),
                ('quantidade', models.PositiveIntegerField(verbose_name='Quantidade')),
                ('imagem', models.CharField(max_length=2000)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedidosmodels', verbose_name='Pedidos itens')),
            ],
            options={
                'verbose_name': 'Pedido item',
                'verbose_name_plural': 'Pedidos itens',
            },
        ),
        migrations.AddIndex(
            model_name='pedidosmodels',
            index=models.Index(fields=['usuario'], name='usuario_pedido_idx'),
        ),
        migrations.AddIndex(
            model_name='itenspedidosmodels',
            index=models.Index(fields=['produto_id'], name='pedido_id_idx'),
        ),
        migrations.AddIndex(
            model_name='itenspedidosmodels',
            index=models.Index(fields=['variacao_id'], name='variacao_id_idx'),
        ),
    ]