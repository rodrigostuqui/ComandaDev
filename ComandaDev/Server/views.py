from django.shortcuts import render, redirect
from .models import Itens, Vendas, Categoria, Mesa

def index(request):
    return render(request, 'index.html')

def mesas(request):
    if request.method == 'POST':
        mesa = request.POST.get('mesa_nome', False)
        form = Mesa()
        form.mesa = mesa
        if(len(Mesa.objects.filter(mesa=mesa)) == 0):
            form.save()
    mesas = Mesa.objects.all()
    return render(request, 'mesas.html', {'mesas': mesas})

def itens(request):
    return render(request, 'itens.html')

def categoria(request):
    return render(request, 'categoria.html')
    
def itensmesa(request):
    if request.method == 'POST':
        mesa = request.POST.get('mesa_id', False)
        dados_venda = Vendas.objects.filter(mesa=mesa)
        mesa = Mesa.objects.filter(mesa=mesa)
    elif request.method == 'GET':
        mesa = request.GET.get('mesa_id', False)
        dados_venda = Vendas.objects.filter(mesa=mesa)
        mesa = Mesa.objects.filter(mesa=mesa)
    return render(request, 'itensmesa.html', {'mesa' : mesa[0].mesa, 'itens': Itens.objects.all().order_by('id'), 'vendas' : dados_venda, 'total' : mesa[0].total_valor, 'recebido': mesa[0].valor_recebido})


def finalizar_venda(request):
    valor_recebido = request.POST.get('recebido')
    mesa = request.POST.get('mesa_id')
    mesa = Mesa.objects.filter(mesa=mesa)
    mesa.update(total_valor=float(str(mesa[0].total_valor))-float(valor_recebido))
    mesa.update(valor_recebido=float(str(mesa[0].valor_recebido))+float(valor_recebido))
    if (float(str(mesa[0].total_valor)) == 0):
        Vendas.objects.filter(mesa=mesa[0].mesa).delete()
        mesa.delete()
    return redirect('mesas')

def atualiza_quantidade(request):
    codigo_item = request.POST.get('codigo_item', False)
    quantidade = request.POST.get('quantidade', False)
    mesa = request.POST.get('mesa_id', False)
    url = f'itensmesa/?mesa_id={mesa}'
    it = Itens.objects.filter(id=codigo_item)
    if(len(Vendas.objects.filter(codigo=codigo_item, mesa=mesa)) != 0):
        venda = Vendas.objects.filter(codigo=codigo_item, mesa=mesa)
        venda.update(quantidade=float(str(venda[0].quantidade))+float(quantidade))
        venda.update(valor=float(str(venda[0].quantidade))*float(str(it[0].valor)))
        if(float(str(venda[0].quantidade)) == 0):
            venda.delete()
    else:
        vendas = Vendas()
        vendas.codigo = it[0].id
        vendas.mesa = mesa
        vendas.nome = it[0].nome
        vendas.categoria = it[0].categoria
        vendas.quantidade = quantidade
        vendas.valor = float(quantidade)*float(str(it[0].valor))
        vendas.save()
    dados_venda = Vendas.objects.filter(mesa=mesa)
    total = 0
    for x in dados_venda:
        total = total + float(str(x.valor))
    mesa = Mesa.objects.filter(mesa=mesa)
    mesa.update(total_valor=total)
    return redirect(url)