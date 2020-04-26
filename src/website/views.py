from django.shortcuts import render
from .models import Rinvio, Ufficio, Giudice
from .forms import RinvioModelForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib import messages 



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

@login_required
def aggiungi_rinvio(request):

    if request.method == 'POST':
        form = RinvioModelForm(request.POST, request.FILES)

        if form.is_valid():
            print('form è valido')
            try:
                nuovo_rinvio = form.save()

                return HttpResponseRedirect(f'/rinvii')

            except Exception as e:
                print('Form non è valido')
                print(e)
        else:
            print('Errore ?')
            print(messages.error(request, "Error"))

    else:
        form = RinvioModelForm()
        context = {"form": form}
        return render(request, 'rinvii/add.html', context)

def carica_giudici(request):
    ufficio_id = request.GET.get('ufficio')
    giudici = Giudice.objects.filter(ufficio=ufficio_id)
    #return render(request, 'dropdown_giudici.html', {'giudici': giudici})
    # data = serializers.serialize("json", giudici)
    data = [{"pk": str(giudice.pk), "giudice": str(giudice)} for giudice in giudici]
    return JsonResponse(data, safe=False)




