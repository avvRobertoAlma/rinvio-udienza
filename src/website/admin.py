from django.contrib import admin
from .models import Giudice, Ufficio, Rinvio


class RinvioAdmin(admin.ModelAdmin):
    list_display = ('ufficio','get_cognome_giudice','data_udienza_rinviata','testo')
    search_fields = ['data_udienza_rinviata', 'testo', 'giudice__cognome']

    def get_cognome_giudice(self, obj):
        return obj.giudice.cognome
    
    get_cognome_giudice.admin_order_field = 'giudice'  # Allows column order sorting
    get_cognome_giudice.short_description = 'Cognome Giudice'  # Renames column head


admin.site.register(Giudice)
admin.site.register(Ufficio)
admin.site.register(Rinvio, RinvioAdmin)

 

