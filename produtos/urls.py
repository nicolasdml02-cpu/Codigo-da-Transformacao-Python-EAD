from django.urls import path
from . import views

urlpatterns = [
    # Rota para listagem com busca e paginação (ex: http://127.0.0.1:8000/produtos/)
    path('', views.listar_produtos, name='listar_produtos'),
    
    # Rota para cadastrar produto (ex: http://127.0.0.1:8000/produtos/cadastrar/)
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    
    # Rota para atualizar produto por ID/PK (ex: http://127.0.0.1:8000/produtos/atualizar/1/)
    path('atualizar/<int:pk>/', views.atualizar_produto, name='atualizar_produto'),
    
    # Rota para excluir produto por ID/PK (ex: http://127.0.0.1:8000/produtos/excluir/1/)
    path('excluir/<int:pk>/', views.excluir_produto, name='excluir_produto'),
]