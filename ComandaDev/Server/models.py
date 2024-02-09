from django.db import models

class Mesa(models.Model):
    mesa = models.CharField(max_length = 100, primary_key = True)
    total_valor = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
    valor_recebido = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
    def __str__(self):
        return self.mesa

class Vendas(models.Model):
    codigo = models.IntegerField(primary_key = True)
    mesa = models.CharField(max_length=100)   
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    impresso = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

class Itens(models.Model):
    id = models.IntegerField(primary_key = True, default = 0)   
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=3)
