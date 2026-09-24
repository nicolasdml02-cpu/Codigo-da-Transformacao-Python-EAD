from django.contrib import admin
from django.test import TestCase
from django.urls import reverse
# Importação do modelo
from modulo14_intro_django_nicolasantana_ativ01 import Produto


# --- PAINEL DE ADMINISTRAÇÃO ---

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'quantidade')
    search_fields = ('nome', 'descricao')
    list_filter = ('preco',)
    list_per_page = 20


# --- TESTES AUTOMATIZADOS ---

class ProdutoModelTest(TestCase):
    def setUp(self):
        self.produto = Produto.objects.create(
            nome="Notebook Gaming",
            descricao="Notebook de alta performance",
            preco=4500.00,
            quantidade=5
        )

    def test_criacao_produto(self):
        self.assertEqual(self.produto.nome, "Notebook Gaming")
        self.assertEqual(self.produto.quantidade, 5)
        self.assertEqual(str(self.produto), "Notebook Gaming - R$ 4500.0")

class ProdutoViewsTest(TestCase):
    def setUp(self):
        self.produto = Produto.objects.create(
            nome="Teclado Mecânico",
            descricao="Teclado RGB",
            preco=250.00,
            quantidade=10
        )

    def test_listagem_produtos_status_code(self):
        response = self.client.get(reverse('listar_produtos'))
        self.assertEqual(response.status_code, 200)

    def test_exclusao_produto(self):
        response = self.client.post(reverse('excluir_produto', args=[self.produto.pk]))
        self.assertEqual(response.status_code, 302) # Redirecionamento após exclusão
        self.assertFalse(Produto.objects.filter(pk=self.produto.pk).exists())