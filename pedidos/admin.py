from django.contrib import admin
from .models import PedidosModels, ItensPedidosModels


class ItensPedidosInline(admin.TabularInline):
    model = ItensPedidosModels
    extra = 1


class PedidosInlineAdmin(admin.ModelAdmin):
    inlines = [
        ItensPedidosInline
    ]


admin.site.register(PedidosModels, PedidosInlineAdmin)
admin.site.register(ItensPedidosModels)