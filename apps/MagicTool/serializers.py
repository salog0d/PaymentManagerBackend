from rest_framework import serializers
from .models import (
    RespuestaBanco, Credito, Banco, Respuesta,
    Emisora, ListaCobro, Cobro, Logs
)


class RespuestaBancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaBanco
        fields = ['id', 'respuesta_banco']


class CreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credito
        fields = ['id', 'id_identifier']


class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = ['id', 'banco']


class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = ['id', 'respuesta']


class EmisoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emisora
        fields = ['id', 'id_banco', 'emisora', 'tipo_envio']


class ListaCobroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaCobro
        fields = ['id', 'fecha_creacion', 'id_banco', 'hora', 'id_emisora']


class CobroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cobro
        fields = [
            'id',
            'id_credito',
            'monto_exigible',
            'monto_cobro',
            'monto_cobrado',
            'id_respuesta_banco',
            'id_banco',
            'id_lista_cobro'
        ]


class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = ['id', 'timestamp', 'level', 'message', 'resultado']
