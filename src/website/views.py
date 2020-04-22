from django.shortcuts import render
from .models import Rinvio, Ufficio, Giudice

# Create your views here.
def lista_Rinvii(request):
    # ottiene la lista di tutti i rinvii dal DB
    rinvii = Rinvio.objects.all().order_by('-created')

    for rinvio in rinvii:

        # prende l'unico giudice associato al rinvio
        giudice = rinvio.giudici.first()

    context = {
        "rinvii":rinvii
    }
    return render(request, 'rinvii/list.html', context)

def dettaglio_rinvio(request, pk):
    rinvio = Rinvio.objects.get(pk=pk)

    context = {
        "rinvio":rinvio
    }
    return render(request, 'rinvii/dettaglio.html', context)