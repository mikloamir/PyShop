from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

# Create your views here.

html = """
<h1>Produtos</h1>
<ul>
    <li>
        item 1
        
    </li>
    <li>
        item 2
    </li>
    <li>
        item 3
    </li>
    <li>
        item 4
    </li>
</ul>
"""

def index(request) :

    telefone = [Produto('Telefone sem fio - Intelbras', 80, 10, 'https://a-static.mlcdn.com.br/1500x1500/telefone-sem-fio-intelbras-ts-2510-id-preto-4122510/bitsbytes/20325/073f5bba1fa3716ff46082aaa0f2f533.jpg')]

    #return HttpResponse(html)
    return render(request, 'index.html', {'produto' : telefone})