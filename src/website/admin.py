from django.contrib import admin
from .models import Giudice, Ufficio, Rinvio



# Register your models here.
admin.site.register(Giudice)
admin.site.register(Ufficio)
admin.site.register(Rinvio)