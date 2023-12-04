from django.urls import path
from . import views


app_name = 'perfil' # perfil:criar


urlpatterns = [
    path('', views.CriarPerfil.as_view(), name='criar'),
    path('atualizar/', views.AtualizarPerfil.as_view(), name='atualizar'),
    path('login/', views.LoginPerfil.as_view(), name='login'),
    path('logout/', views.LogoutPerfil.as_view(), name='logout'),
]
