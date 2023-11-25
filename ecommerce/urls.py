from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('produtos/', include('produtos.urls')),
    # path('pedidos/', include('pedidos.urls')),
    # path('perfils/', include('perfils.urls')),
    
    # TODO somente desenvolvimento, apagar no deploy
    path('__debug__/', include('debug_toolbar.urls')),
]


# configurando arquivos statics servindo ao DJANGO
# necessário importa do settings, o MEDIA_URL E MEDIA_ROOT
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)