from django.shortcuts import render
from django.core.paginator import Paginator
# Importação do modelo
from modulo14_intro_django_nicolasantana_ativ01 import Produto


def listar_produtos_com_busca_e_paginacao(request):
    """
    View de listagem avançada com suporte a filtro de busca por nome 
    e paginação contendo 5 itens por página.
    """
    busca = request.GET.get('busca', '')
    
    # Filtro opcional por nome
    if busca:
        produtos_list = Produto.objects.filter(nome__icontains=busca)
    else:
        produtos_list = Produto.objects.all()

    # Configuração da Paginação (5 produtos por página)
    paginator = Paginator(produtos_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'busca': busca,
    }
    return render(request, 'produtos/listar_desafio.html', context)