from django.urls import path
from . import views


app_name = 'pedido' # pedido:pagar


urlpatterns = [
    path('', views.PagarPedido.as_view(), name='pagar'),
    path('fecharpedido/', views.FecharPedido.as_view(), name='fechar'),
    path('detalhepedido/', views.DetalhePedido.as_view(), name='detalhe'),
]
