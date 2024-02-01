from django.db import models

class Mesa(models.Model):
    mesa = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.nome

class Vendas(models.Model):
    codigo = models.IntegerField()
    mesa = models.CharField(max_length=100)   
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=3)
    quantidade = models.DecimalField(max_digits=10, decimal_places=3)

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

class Itens(models.Model):
    id = models.IntegerField(primary_key = True, default = 0)   
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=3)
