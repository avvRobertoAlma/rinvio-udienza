from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('uffici', views.lista_uffici, name="lista uffici"),
    path('uffici/<int:pk>', views.dettaglio_ufficio, name="dettaglio ufficio"),
    path('giudici', views.lista_uffici, name="lista giudici"),
    path('giudici/<int:pk>', views.dettaglio_giudice, name="dettaglio giudice"),
    path('rinvii', views.lista_Rinvii, name="lista rinvii"),
    path('rinvii/<int:pk>', views.dettaglio_rinvio, name="dettaglio rinvio")
]


