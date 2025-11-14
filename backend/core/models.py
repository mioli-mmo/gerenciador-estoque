from django.db import models

# Create your models here.
'''
[] Criação dos models
[] método __str__
'''

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_digits=14, null=True, blank=True)
    telefone = models.CharField(max_digits=13)
    email = models.CharField(max_length=255, null=True, blank=True)

class Fornecedor(models.Model):
    class Tipo(models.TextChoices):
        PESSOA = "P", "Pessoa"
        EMPRESA = "E", "Empresa"

    cnpj_cpf = models.CharField(max_digits=18, null=True, blank=True)
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_digits=13)
    email = models.CharField(max_length=255, null=True, blank=True)
    tipo = models.CharField(max_digits=1, choices=Tipo, default=Tipo.EMPRESA)

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade_estoque = models.SmallIntegerField()
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Movimentacao(models.Model):
    class Tipo(models.TextChoices):
        PEDIDO = "PE", "Pedido"
        VENDA = "VE", "Venda"

    valor_total = models.DecimalField(max_digits=7, decimal_places=2)
    data = models.DateField()
    tipo = models.CharField(max_digits=2, choices=Tipo)
    fornecedor_id = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True, blank=True)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)

class Produto_movimentacao(models.Model):
    valor_unitario = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade_movimentacao = models.SmallIntegerField()
    valor_movimentacao = models.DecimalField(max_digits=7, decimal_places=2)
    produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)
    movimentacao_id = models.ForeignKey(Movimentacao, on_delete=models.CASCADE)