from django.db import models

class RespuestaBanco(models.Model):
    id = models.AutoField(primary_key=True)
    respuesta_banco = models.CharField(
        max_length=100,
        choices=[
            ('RespuestaBanco1', 'RespuestaBanco1'),
            ('RespuestaBanco2', 'RespuestaBanco2'),
            ('RespuestaBanco3', 'RespuestaBanco3'),
            ('RespuestaBanco4', 'RespuestaBanco4'),
            ('RespuestaBanco5', 'RespuestaBanco5'),
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
            ('Banco1', 'Banco1'),
            ('Banco2', 'Banco2'),
            ('Banco3', 'Banco3'),
            ('Banco4', 'Banco4'),
            ('Banco5', 'Banco5'),
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
    emisora = models.CharField(
        max_length=100,
        choices=[
            ('Emisora1', 'Emisora1'),
            ('Emisora2', 'Emisora2'),
            ('Emisora3', 'Emisora3'),
            ('Emisora4', 'Emisora4'),
            ('Emisora5', 'Emisora5'),
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
    

