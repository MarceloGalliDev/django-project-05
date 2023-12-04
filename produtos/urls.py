from django.urls import path
from . import views


app_name = 'produto' # produto:lista

urlpatterns = [
    path('', views.ListaProduto.as_view(), name='lista'),
    path('<slug>/', views.DetalheProduto.as_view(), name='detalhe'),
    path('addcart/', views.AddCartProduto.as_view(), name='addcart'),
    path('delcart/', views.DelCartProduto.as_view(), name='delcart'),
    path('listcart/', views.ListCartProduto.as_view(), name='listcart'),
    path('endcart/', views.EndCartProduto.as_view(), name='endcart'),
]
