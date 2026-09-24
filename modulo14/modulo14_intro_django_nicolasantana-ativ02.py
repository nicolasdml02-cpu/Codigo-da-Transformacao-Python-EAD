from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path
from django.forms import ModelForm
# Importação do modelo definido no exercício 1
from modulo14_intro_django_nicolasantana_ativ01 import Produto


# Form para criação e edição de produtos
class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade']


# --- VIEWS ---

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/form.html', {'form': form, 'titulo': 'Cadastrar Produto'})

def atualizar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/form.html', {'form': form, 'titulo': 'Atualizar Produto'})

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')
    return render(request, 'produtos/confirmar_exclusao.html', {'produto': produto})


# --- ROTAS / URLS ---

urlpatterns = [
    path('', listar_produtos, name='listar_produtos'),
    path('cadastrar/', cadastrar_produto, name='cadastrar_produto'),
    path('atualizar/<int:pk>/', atualizar_produto, name='atualizar_produto'),
    path('excluir/<int:pk>/', excluir_produto, name='excluir_produto'),
]