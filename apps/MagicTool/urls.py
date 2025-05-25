from django.urls import path
from .views import (
    # RespuestaBanco
    RespuestaBancoListCreateView,
    RespuestaBancoDetailView,
    
    # Credito
    CreditoListCreateView,
    CreditoDetailView,
    
    # Banco
    BancoListCreateView,
    BancoDetailView,
    
    # Respuesta
    RespuestaListCreateView,
    RespuestaDetailView,
    
    # Emisora
    EmisoraListCreateView,
    EmisoraDetailView,
    
    # ListaCobro
    ListaCobroListCreateView,
    ListaCobroDetailView,
    
    # Cobro
    CobroListCreateView,
    CobroDetailView,
    
    # Logs
    LogsListCreateView,
    LogsDetailView,
)

app_name = 'magic_tool'

urlpatterns = [
    # RespuestaBanco endpoints
    path('respuestas-banco/', RespuestaBancoListCreateView.as_view(), name='respuestas_banco_list'),
    path('respuestas-banco/<int:pk>/', RespuestaBancoDetailView.as_view(), name='respuestas_banco_detail'),
    
    # Credito endpoints
    path('creditos/', CreditoListCreateView.as_view(), name='creditos_list'),
    path('creditos/<int:pk>/', CreditoDetailView.as_view(), name='creditos_detail'),
    
    # Banco endpoints
    path('bancos/', BancoListCreateView.as_view(), name='bancos_list'),
    path('bancos/<int:pk>/', BancoDetailView.as_view(), name='bancos_detail'),
    
    # Respuesta endpoints
    path('respuestas/', RespuestaListCreateView.as_view(), name='respuestas_list'),
    path('respuestas/<int:pk>/', RespuestaDetailView.as_view(), name='respuestas_detail'),
    
    # Emisora endpoints
    path('emisoras/', EmisoraListCreateView.as_view(), name='emisoras_list'),
    path('emisoras/<int:pk>/', EmisoraDetailView.as_view(), name='emisoras_detail'),
    
    # ListaCobro endpoints
    path('listas-cobro/', ListaCobroListCreateView.as_view(), name='listas_cobro_list'),
    path('listas-cobro/<int:pk>/', ListaCobroDetailView.as_view(), name='listas_cobro_detail'),
    
    # Cobro endpoints
    path('cobros/', CobroListCreateView.as_view(), name='cobros_list'),
    path('cobros/<int:pk>/', CobroDetailView.as_view(), name='cobros_detail'),
    
    # Logs endpoints
    path('logs/', LogsListCreateView.as_view(), name='logs_list'),
    path('logs/<int:pk>/', LogsDetailView.as_view(), name='logs_detail'),
]