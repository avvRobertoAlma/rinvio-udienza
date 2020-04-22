from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.lista_Rinvii, name="lista rinvii"),
    path('<int:pk>', views.dettaglio_rinvio, name="dettaglio rinvio")
]