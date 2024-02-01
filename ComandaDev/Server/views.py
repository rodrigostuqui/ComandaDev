from django.shortcuts import render, redirect
from .models import Itens, Vendas, Categoria, Mesa

def index(request):
    return render(request, 'index.html')

def mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'mesas.html', {'mesas': mesas})

def itens(request):
    return render(request, 'itens.html')

def categoria(request):
    return render(request, 'categoria.html')

def criamesa(request):
    if request.method == 'POST':
        form = Mesa()
        form.mesa = request.POST.get('dado_texto', False)
        form.save()
        return redirect('mesas')
    else:
        return render(request, 'criamesa.html')
    
def itensmesa(request):
    return render(request, 'itensmesa.html')