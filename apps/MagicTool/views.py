from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import (
    RespuestaBanco, Credito, Banco, Respuesta,
    Emisora, ListaCobro, Cobro, Logs
)
from .serializers import (
    RespuestaBancoSerializer, CreditoSerializer, BancoSerializer,
    RespuestaSerializer, EmisoraSerializer, ListaCobroSerializer,
    CobroSerializer, LogsSerializer
)

# RespuestaBanco
class RespuestaBancoListCreateView(generics.ListCreateAPIView):
    queryset = RespuestaBanco.objects.all()
    serializer_class = RespuestaBancoSerializer
    permission_classes = [IsAuthenticated]

class RespuestaBancoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RespuestaBanco.objects.all()
    serializer_class = RespuestaBancoSerializer
    permission_classes = [IsAuthenticated]


# Credito
class CreditoListCreateView(generics.ListCreateAPIView):
    queryset = Credito.objects.all()
    serializer_class = CreditoSerializer
    permission_classes = [IsAuthenticated]

class CreditoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Credito.objects.all()
    serializer_class = CreditoSerializer
    permission_classes = [IsAuthenticated]


# Banco
class BancoListCreateView(generics.ListCreateAPIView):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer
    permission_classes = [IsAuthenticated]

class BancoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer
    permission_classes = [IsAuthenticated]


# Respuesta
class RespuestaListCreateView(generics.ListCreateAPIView):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer
    permission_classes = [IsAuthenticated]

class RespuestaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer
    permission_classes = [IsAuthenticated]


# Emisora
class EmisoraListCreateView(generics.ListCreateAPIView):
    queryset = Emisora.objects.all()
    serializer_class = EmisoraSerializer
    permission_classes = [IsAuthenticated]

class EmisoraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emisora.objects.all()
    serializer_class = EmisoraSerializer
    permission_classes = [IsAuthenticated]


# ListaCobro
class ListaCobroListCreateView(generics.ListCreateAPIView):
    queryset = ListaCobro.objects.all()
    serializer_class = ListaCobroSerializer
    permission_classes = [IsAuthenticated]

class ListaCobroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListaCobro.objects.all()
    serializer_class = ListaCobroSerializer
    permission_classes = [IsAuthenticated]


# Cobro
class CobroListCreateView(generics.ListCreateAPIView):
    queryset = Cobro.objects.all()
    serializer_class = CobroSerializer
    permission_classes = [IsAuthenticated]

class CobroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cobro.objects.all()
    serializer_class = CobroSerializer
    permission_classes = [IsAuthenticated]


# Logs
class LogsListCreateView(generics.ListCreateAPIView):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
    permission_classes = [IsAuthenticated]

class LogsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
    permission_classes = [IsAuthenticated]
