from django.contrib import admin

from .forms import \
    MeuModeloForm  # Importa o formulário personalizado com CKEditor 5
from .models import MeuModelo  # Substitua pelo nome correto do seu modelo


class MeuModeloAdmin(admin.ModelAdmin):
    form = MeuModeloForm  # Aplica o formulário customizado com CKEditor 5 no admin

    list_display = (
        'id',
        'titulo',
        'usuario_criador',
        'data_created',
        'data_updated',
    )
    list_filter = ('usuario_criador',)
    search_fields = ('titulo', 'usuario_criador__username')
    readonly_fields = ('data_created', 'data_updated')


admin.site.register(MeuModelo, MeuModeloAdmin)
