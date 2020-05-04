from django.db import models
from django.conf import settings

# Create your models here.
class Ufficio(models.Model):
    class Meta:
        verbose_name ="Ufficio"
        verbose_name_plural="Uffici"

    denominazione = models.CharField(max_length=400, unique=True)
    codice_ufficio = models.CharField(max_length=400, unique=True)

    def __str__(self):
        return self.denominazione




class Giudice(models.Model):
    class Meta:
        verbose_name ="Giudice"
        verbose_name_plural="Giudici"

    ufficio = models.ForeignKey(Ufficio, on_delete=models.CASCADE, related_name="giudici")
    nome = models.CharField(max_length=500)
    cognome = models.CharField(max_length=500)
    sezione = models.CharField(max_length=500, blank=True)
    def __str__(self):
        if self.sezione:
            return f"{self.cognome} {self.nome} - Sezione: {self.sezione}"
        else: 
            return f"{self.cognome} {self.nome}"


class Rinvio(models.Model):
    class Meta:
        verbose_name ="Rinvio"
        verbose_name_plural="Rinvii"

    ufficio = models.ForeignKey(Ufficio, on_delete=models.CASCADE, related_name="rinvii")
    giudice = models.ForeignKey(Giudice, on_delete=models.CASCADE, related_name="rinvii")
    data_udienza_rinviata = models.DateField(blank=True, null=True)
    data_rinvio = models.DateField(blank=True, null=True)
    testo = models.TextField(blank=True)
    immagine = models.ImageField(blank=True, upload_to='img')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rinvio caricato in data {self.created}"