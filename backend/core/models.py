from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    # ...

class Fornecedor(models.Model):
    nome = models.CharField(max_length=150)
    # ...

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    # ...

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    # ...

class Movimentacao(models.Model):
    valor_total = models.DecimalField(max_digits=7, decimal_places=2)
    # ...

class Produto_movimentacao(models.Model):
    valor_unitario = models.DecimalField(max_digits=7, decimal_places=2)
    # ...