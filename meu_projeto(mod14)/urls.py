from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Rota para o painel de administração do Django
    path('admin/', admin.site.urls),
    
    # Inclui todas as rotas criadas dentro do app 'produtos'
    path('produtos/', include('produtos.urls')),
]