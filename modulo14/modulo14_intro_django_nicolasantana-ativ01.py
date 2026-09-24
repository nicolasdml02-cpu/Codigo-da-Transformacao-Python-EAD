from django.db import models

class Produto(models.Model):
    """
    Modelo referente ao cadastro de produtos no sistema.
    """
    nome = models.CharField(max_length=100, verbose_name="Nome do Produto")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    quantidade = models.IntegerField(default=0, verbose_name="Quantidade em Estoque")

    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome']