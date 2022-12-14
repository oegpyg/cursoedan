from django.shortcuts import render
from .models import FaseGrupos, FaseGruposPaises
from django.http import JsonResponse
import time


def home(request):
    # a traves de las fases de grupo quiero saber que paises estan en ellas
    fasegrupos = FaseGrupos.objects.all()
    data = []
    for i in fasegrupos:
        row = {'grupo': i.nombre, 'paises': []}
        for o in i.fasegrupospaises_set.all():
            row['paises'].append(
                {'nombre': o.pais.nombre, 'codigo': o.pais.codigo, 'icono': o.pais.imagen})
        data.append(row)

    return render(request, 'home.html', {'fg': data})


def getFGP(request):
    # a traves de las fases de grupo quiero saber que paises estan en ellas
    fasegrupos = FaseGrupos.objects.all()
    data = []
    for i in fasegrupos:
        row = {'grupo': i.nombre, 'paises': []}
        for o in i.fasegrupospaises_set.all():
            row['paises'].append(
                {'nombre': o.pais.nombre, 'codigo': o.pais.codigo, 'icono': o.pais.imagen})
        data.append(row)
    time.sleep(10)
    return JsonResponse(data, safe=False)
