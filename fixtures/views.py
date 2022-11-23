from django.shortcuts import render
from .models import FaseGrupos


def home(request):
    fasegrupo = FaseGrupos.objects.all()

    return render(request, 'home.html', {'fg': fasegrupo})
