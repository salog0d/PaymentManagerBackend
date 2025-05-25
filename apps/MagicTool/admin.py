from django.contrib import admin
from .models import RespuestaBanco, Credito, Banco, Respuesta, Emisora, ListaCobro, Cobro, Logs
# Register your models here.
admin.site.register([RespuestaBanco, 
                     Credito, 
                     Banco, 
                     Respuesta, 
                     Emisora, 
                     ListaCobro, 
                     Cobro, 
                     Logs])  # Register your models here.