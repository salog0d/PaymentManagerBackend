from django.db import models

class RespuestaBanco(models.Model):
    id = models.AutoField(primary_key=True)
    respuesta_banco = models.CharField(
        max_length=100,
        choices=[
            ('0', 'Domiciliacion Exitosa'),
            ('1', 'Cuenta Inexistente'),
            ('2', 'Cuenta Bloqueada'),
            ('3', 'Cuenta Cancelada'),
            ('4', 'Cuenta Insuficiencia Fondos'),
            ('5', 'Cuenta en otra divisa'),
            ('6', 'Cuenta no pertenece al Banco Cliente Usuario'),
            ('7', 'Transaccion Duplicada'),
            ('8', 'Orden de no pagara a ese Emisor'),
            ('9', 'Importe mayor al autorizado por el cliente'),
            ('10', 'Domiciliacion dada de  baja'),
            ('11', 'Cuenta sin autorizacion para domiciliar'),
            ('12', 'Cliente desconoce cargo'),
            ('13', 'Otras causas'),
            ('14', 'Cuenta correcta en la validacion de cuentas'),
            ('15', 'Operacion fuera de horario'),
            ('16', 'Caracteres Invalidos'),
            ('17', 'Dato erroneo o invalido'),
            ('18', 'Error en proceso de Domiciliacion'),
            ('19', 'Operacion Invalida'),
            ('20', 'Domiciliacion Existe'),
            ('21', 'Baja por oficina'),
            ('22', 'Error de proceso'),
            ('23', 'Cuenta con todas las domiciliaciones dadas de baja'),
            ('24', 'Cuenta no admite domiciliaciones'),
            ('25', 'Domiciliacion no realizada'),
            ('26', 'Bajo Pago'),
            ('51', 'Cuenta inexistente'),
            ('52', 'Cuenta bloqueada'),
            ('53', 'Cuenta cancelada'),
            ('81', 'Operación recibida fuera de horario'),
            ('82', 'Caracteres inválidos'),
            ('83', 'Bin inválido'),
            ('88', 'Bloqueo a todos los cargos'),
            ('99', 'Cuenta Correcta en la validación de cuentas'),
            ('D090', 'Inconsistencia en la Cuenta Clabe'),
            ('D091', 'Inconsistencia en la Cuenta Clabe'),
            ('D092', 'Inconsistencia en la Cuenta Clabe'),
            ('D093', 'Inconsistencia en la Cuenta Clabe'),
            ('D094', 'Inconsistencia en la Cuenta Clabe'),
            ('D095', 'Inconsistencia en la Cuenta Clabe'),
            ('D096', 'Inconsistencia en la Cuenta Clabe'),
            ('D097', 'Inconsistencia en la Cuenta Clabe'),
            ('D098', 'Inconsistencia en la Cuenta Clabe'),
            ('D099', 'Inconsistencia en la Cuenta Clabe'),
            ('D100', 'Inconsistencia en la Cuenta Clabe'),
            ('DD00001', 'Cuenta con Insuficiencia de Fondos'),
            ('DD00019', 'Cuenta con Insuficiencia de Fondos'),
            ('DD00020', 'Reverso del cargo a solicitud del cliente'),
            ('DD00021', 'Cuenta Inexistente'),
            ('DD00022', 'Cuenta con Insuficiencia de Fondos'),
            ('DD00023', 'Transacción rechazada'),
            ('DD00024', 'No se proceso cargo'),
            ('DD00025', 'Cuenta Bloqueada'),
            ('DD00026', 'Cuenta Cancelada'),
            ('DD00027', 'Transacción rechazada'),
            ('DD00028', 'Importe mayor al autorizado por el cliente'),
            ('DD00029', 'Transacción rechazada'),
            ('DD00030', 'Domiciliacion no realizada'),
            ('DD00031', 'Cuenta con Insuficiencia de Fondos'),
            ('DD00033', 'Domiciliacion dada de baja'),
            ('DD00034', 'Transacción rechazada'),
            ('DD00035', 'Transacción rechazada'),
            ('DD00036', 'ENTREGADO'),
            ('DD00037', 'TRANSACCION RECHAZADA'),
            ('DD00038', 'TRANSACCIÓN RECHAZADA (OGE0076)'),
            ('DD00039', 'TRANSACCIÓN RECHAZADA (OGE0039)'),
            ('DD00040', 'TRANSACCIÓN RECHAZADA (OGE0041)'),
            ('DOM1', 'Domiciliacion Exitosa'),
            ('DOM10', 'Cuenta Bloqueada'),
            ('DOM11', 'Transacción rechazada'),
            ('DOM12', 'Por orden del cliente: cancelación del servicio'),
            ('DOM13', 'Por orden del cliente: no pagar a ese emisor'),
            ('DOM14', 'Transaccion Duplicada'),
            ('DOM2', 'Cuenta con Insuficiencia de Fondos'),
            ('DOM3', 'Transacción rechazada'),
            ('DOM4', 'Domiciliacion dada de baja'),
            ('DOM5', 'Cuenta Cancelada'),
            ('DOM6', 'Cuenta con Insuficiencia de Fondos'),
            ('DOM7', 'Cuenta Inexistente'),
            ('DOM8', 'Reverso del cargo a solicitud del cliente'),
            ('DOM9', 'Importe mayor al autorizado por el cliente'),
            ('INC0', 'Domiciliacion Exitosa'),
            ('INC1', 'Defuncion'),
            ('INC10', 'Convenio cerrado'),
            ('INC11', 'Instalando'),
            ('INC15', 'Fraude'),
            ('INC16', 'Cuenta Bloqueada'),
            ('INC17', 'Dejo de pagar'),
            ('INC18', 'Pago irregular'),
            ('INC19', 'Liquida con virtual'),
            ('INC2', 'Baja por jubilación'),
            ('INC21', 'Fuera de politica'),
            ('INC22', 'Liquida con transito'),
            ('INC23', 'Saldo menor a cuota'),
            ('INC3', 'Baja dependencia'),
            ('INC4', 'Licencia'),
            ('INC5', 'Amparo'),
            ('INC6', 'Sin liquidez'),
            ('INC7', 'Bajo pago'),
            ('INC8', 'Sin pago'),
            ('INC9', 'Cuenta Cancelada'),
            ('DD00041', 'TRANSACCIÓN RECHAZADA (OGE0076)'),
            ('DD00042', 'TRANSACCIÓN RECHAZADA (OGE0039)'),
            ('DD00043', 'EN'),
        ]
    )



    def __str__(self):
        return self.respuesta_banco

class Credito(models.Model):
    id = models.AutoField(primary_key=True)
    id_identifier= models.IntegerField()

class Banco(models.Model):
    id = models.AutoField(primary_key=True)
    banco = models.CharField(
        max_length=100,
        choices=[
            ('1', 'BANCO DE MEXICO (BANXICO)'),
            ('101', 'BANCA CREMI'),
            ('102', 'ABN AMRO BANK MEXICO'),
            ('103', 'AMERICAN EXPRESS'),
            ('106', 'BANK OF AMERICA'),
            ('107', 'BANCO DE BOSTON'),
            ('108', 'BANK OF TOKYO'),
            ('110', 'JP MORGAN'),
            ('112', 'COMERICA BANK'),
            ('113', 'BANCO VE POR MAS'),
            ('116', 'ING BANK'),
            ('12', 'BBVA MEXICO'),
            ('124', 'DEUTSCHE BANK'),
            ('126', 'CREDIT SUIZA'),
            ('127', 'AZTECA'),
            ('128', 'AUTOFIN MEXICO, S. A.'),
            ('129', 'BARCLAYS BANK MEXICO'),
            ('131', 'BANCO FAMSA'),
            ('132', 'BMULTIVA'),
            ('135', 'NAFIN'),
            ('137', 'BANCOPPEL'),
            ('14', 'SANTANDER'),
            ('149', 'BANRURAL'),
            ('166', 'BABIEN'),
            ('168', 'HIPOTECARIA FED'),
            ('19', 'BANJERCITO'),
            ('2', 'BANAMEX'),
            ('21', 'HSBC'),
            ('22', 'G.E. CAPITAL'),
            ('3', 'BANCA SERFIN'),
            ('30', 'BANCO DEL BAJIO'),
            ('32', 'IXE'),
            ('36', 'INBURSA'),
            ('37', 'INTERACCIONES'),
            ('42', 'MIFEL'),
            ('44', 'SCOTIABANK'),
            ('58', 'BANREGIO'),
            ('59', 'INVEX'),
            ('6', 'BANCOMEXT'),
            ('60', 'BANSI'),
            ('600', 'CASA DE BOLSA MONEX'),
            ('601', 'CASA DE BOLSA GBM'),
            ('602', 'MASARI CASA DE BOLSA'),
            ('605', 'VALUE CASA DE BOLSA'),
            ('607', 'CASA DE CAMBIO TIBER'),
            ('608', 'CASA DE BOLSA VECTOR'),
            ('610', 'B Y B CASA DE CAMBIO'),
            ('611', 'INTERCAM CASA DE CAMBIO'),
            ('612', 'MAJAPARA CASA DE CAMBIO'),
            ('613', 'MULTIVALORES CASA DE BOLSA'),
            ('614', 'ACCIVAL CASA DE BOLSA'),
            ('615', 'MERRIL LYNCH CASA DE BOLSA'),
            ('616', 'CASA DE BOLSA FINAMEX'),
            ('62', 'AFIRME'),
            ('7', 'CITIBANK, S. A.'),
            ('72', 'BANORTE'),
            ('86', 'BANCEN'),
            ('9', 'BANOBRAS'),
            ('90646', 'STP'),
            ('9999', 'GASTOS DE COBRANZA'),
        ]
    )

    def __str__(self):
        return self.banco
    
class Respuesta(models.Model):
    id = models.AutoField(primary_key=True)
    respuesta = models.CharField(
        max_length=100,
        choices=[
            ('Respuesta1', 'Respuesta1'),
            ('Respuesta2', 'Respuesta2'),
            ('Respuesta3', 'Respuesta3'),
            ('Respuesta4', 'Respuesta4'),
            ('Respuesta5', 'Respuesta5'),
        ]
    )

    def __str__(self):
        return self.respuesta
    
class Emisora(models.Model):
    id = models.AutoField(primary_key=True)

    id_banco = models.IntegerField(
        choices=[
            (2, 'BANAMEX'),
            (12, 'BBVA MEXICO'),
            (14, 'SANTANDER'),
            (72, 'BANORTE'),
        ]
    )

    emisora = models.CharField(
        max_length=100,
        choices=[
            ('NoAplica', 'NoAplica'),
            ('REINTENTO', 'REINTENTO'),
            ('623', '623'),
            ('496', '496'),
            ('639', '639'),
            ('7167', '7167'),
            ('6114', '6114'),
            ('7455', '7455'),
            ('6111', '6111'),
        ]
    )

    tipo_envio = models.CharField(
        max_length=100,
        choices=[
            ('TRADICIONAL', 'TRADICIONAL'),
            ('CUENTA', 'CUENTA'),
            ('TARJETA', 'TARJETA'),
            ('INTERBANCARIO', 'INTERBANCARIO'),
            ('REINTENTO', 'REINTENTO'),
            ('EN LINEA', 'EN LINEA'),
            ('MATUTINO', 'MATUTINO'),
            ('PARCIAL', 'PARCIAL'),
            ('REINTENTO CUENTA', 'REINTENTO CUENTA'),
        ]
    )



    def __str__(self):
        return self.emisora


class ListaCobro(models.Model):

    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id_banco = models.ForeignKey('Banco', on_delete=models.CASCADE)
    hora = models.TimeField()
    id_emisora = models.ForeignKey('Emisora', on_delete=models.CASCADE)

    def __str__(self):
        return self.banco



class Cobro(models.Model):

    id = models.AutoField(primary_key=True)
    id_credito = models.ForeignKey('Credito', on_delete=models.CASCADE)
    monto_exigible = models.DecimalField(max_digits=10, decimal_places=2)
    monto_cobro = models.DecimalField(max_digits=10, decimal_places=2)
    monto_cobrado = models.DecimalField(max_digits=10, decimal_places=2)
    id_respuesta_banco = models.ForeignKey('RespuestaBanco', on_delete=models.CASCADE)
    id_banco = models.ForeignKey('Banco', on_delete=models.CASCADE)
    id_lista_cobro = models.ForeignKey('ListaCobro', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_credito} - {self.monto_exigible} - {self.monto_cobro} - {self.monto_cobrado} - {self.id_respuesta_banco} - {self.id_banco} - {self.id_lista_cobro}"



# Create your models here.
class Logs(models.Model):

    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=10)
    message = models.TextField()
    resultado = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{self.timestamp} - {self.level} - {self.message}"
    

