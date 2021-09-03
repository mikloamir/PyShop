from django.db import models

# Create your models here.

class Produto(models.Model) :

    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    estoque = models.IntegerField()
    url_imagem = models.CharField(max_length=2000)

    def __init__(self, nome, preco, estoque, url) :
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.url_imagem = url
        