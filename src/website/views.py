from django.shortcuts import render
from .models import Rinvio, Ufficio, Giudice

# Create your views here.

def homepage(request): 
    return render(request, 'index.html')

def lista_uffici(request):
    uffici = Ufficio.objects.all()
    context = {
        "uffici":uffici
    }
    return render(request, 'uffici/list.html', context)

def dettaglio_ufficio(request, pk):
    ufficio = Ufficio.objects.get(pk=pk)

    context = {
        "ufficio":ufficio
    }
    return render(request, 'uffici/dettaglio.html', context)

def lista_giudici(request):
    giudici = Giudice.objects.all()
    context = {
        "giudici":giudici
    }
    return render(request, 'giudici/list.html', context)

def dettaglio_giudice(request, pk):
    giudice = Giudice.objects.get(pk=pk)

    context = {
        "giudice":giudice
    }
    return render(request, 'uffici/giudici/dettaglio.html', context)

def lista_Rinvii(request):
    # ottiene la lista di tutti i rinvii dal DB
    rinvii = Rinvio.objects.all().order_by('-created')

    for rinvio in rinvii:
        print(rinvio.giudici)
        

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