from django.shortcuts import render
from .models import Rinvio, Ufficio, Giudice
from .forms import RinvioModelForm, RinvioGiudiceModelForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib import messages 
from django.core.paginator import Paginator

from datetime import datetime, timedelta



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
    giudici = ufficio.giudici.all().order_by('cognome')

    # Codice per pagination
    paginator = Paginator(giudici, 5) # mostra 5 rinvii per pagina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "ufficio":ufficio,
    }
    context["page_obj"] = page_obj

    return render(request, 'uffici/dettaglio.html', context)

def lista_giudici(request):
    giudici = Giudice.objects.all().order_by('cognome')
    
    # Codice per pagination
    paginator = Paginator(giudici, 5) # mostra 5 rinvii per pagina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context["page_obj"] = page_obj

    return render(request, 'giudici/list.html', context)

def dettaglio_giudice(request, pk):
    giudice = Giudice.objects.get(pk=pk)
    rinvii = giudice.rinvii.all().order_by('-data_udienza_rinviata')

     # Codice per pagination
    paginator = Paginator(rinvii, 5) # mostra 5 rinvii per pagina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "giudice":giudice
    }
    context["page_obj"] = page_obj

    
    return render(request, 'uffici/giudici/dettaglio.html', context)

@login_required
def aggiungi_rinvio_giudice(request, pk):
    giudice = Giudice.objects.get(pk=pk)

    if request.method == 'POST':
        form = RinvioGiudiceModelForm(request.POST, request.FILES)

        if form.is_valid():
            print('form è valido')
            try:
                nuovo_rinvio = Rinvio(ufficio=giudice.ufficio, giudice=giudice, data_udienza_rinviata=form.cleaned_data['data_udienza_rinviata'], data_rinvio=form.cleaned_data['data_rinvio'], testo=form.cleaned_data['testo'], immagine=form.cleaned_data['immagine'])
                nuovo_rinvio.save()

                return HttpResponseRedirect(f'/giudici/{giudice.pk}')

            except Exception as e:
                print('Form non è valido')
                print(e)
        else:
            print('Errore ?')
            print(messages.error(request, "Error"))

    else:
        form = RinvioGiudiceModelForm()
        context = {"form": form}
        return render(request, 'uffici/giudici/add_rinvio.html', context)

def lista_Rinvii(request):
    # verifica se ci sono query nella richiesta
    # se non viene passato il parametro "to_date" cerca tutte le udienze rinviate dei prossimi 90 giorni
    if 'filter' in request.GET:
        if 'from_date' in request.GET:
            if len(request.GET['from_date']) > 1:
                from_date = request.GET['from_date']
            else:
                from_date = '2020-04-01'
        else:
            from_date = '2020-04-01'

        if 'to_date' in request.GET:
            if len(request.GET['to_date']) > 1:
                to_date = request.GET['to_date']
            else:
                to_date = datetime.now() + timedelta(days=90)
        else:
            to_date = datetime.now() + timedelta(days=90)



        rinvii = Rinvio.objects.filter(giudice__cognome__icontains=request.GET['giudice'],data_udienza_rinviata__gte=from_date,data_udienza_rinviata__lte=to_date).order_by('-data_udienza_rinviata')
    else:
        # ottiene la lista di tutti i rinvii dal DB
        rinvii = Rinvio.objects.all().order_by('-data_udienza_rinviata')

    # Codice per pagination
    paginator = Paginator(rinvii, 5) # mostra 5 rinvii per pagina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {}
    context["page_obj"] = page_obj
        
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

@login_required
# elimina un rinvio
# @param pk è id del rinvio da eliminare
def elimina_rinvio(request, pk):
    rinvio = Rinvio.objects.get(pk=pk)
    rinvio.delete()
    return HttpResponseRedirect(f'/rinvii')


def carica_giudici(request):
    ufficio_id = request.GET.get('ufficio')
    giudici = Giudice.objects.filter(ufficio=ufficio_id).order_by('cognome')
    #return render(request, 'dropdown_giudici.html', {'giudici': giudici})
    # data = serializers.serialize("json", giudici)
    data = [{"pk": str(giudice.pk), "giudice": str(giudice)} for giudice in giudici]
    return JsonResponse(data, safe=False)

def chi_siamo(request):
    return render(request, 'chi_siamo.html')




