from django.contrib import admin
from .models import Proyecto,tipo_proyecto,curso,imagen

admin.site.register(Proyecto)
admin.site.register(tipo_proyecto)
admin.site.register(curso)
admin.site.register(imagen)

# Relación entre detalle y factura, unirlos en una vista.

