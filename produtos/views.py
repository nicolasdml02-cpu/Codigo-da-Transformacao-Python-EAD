from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade']

def listar_produtos(request):
    busca = request.GET.get('busca', '')
    if busca:
        produtos_list = Produto.objects.filter(nome__icontains=busca)
    else:
        produtos_list = Produto.objects.all()

    paginator = Paginator(produtos_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'produtos/listar.html', {'page_obj': page_obj, 'busca': busca})

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