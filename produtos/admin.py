from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'quantidade')
    search_fields = ('nome', 'descricao')
    list_filter = ('preco',)
    list_per_page = 20