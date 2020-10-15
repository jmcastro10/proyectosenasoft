from django.db import models

class Pacientes(models.Model):
    _idPacientes = models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)
    Dni=models.CharField(max_length=10)
    Fecha_nacimiento=models.DateField
    Direccion=models.CharField(max_length=50)
    Telefono=models.IntegerField(max_length=10)
    Estrato=models.CharField(max_length=1)
    correo=models.EmailField (max_length = 50)

    class Meta:
        verbose_name='paciente'
        verbose_name_plural='pacientes'

    def _str_(self):
        return self.Nombre

class Historial(models.Model):
    _idHistorial=models.AutoField(primary_key=True)
    Observacion=models.CharField(max_length=50)
    Aprobacion=models.IntegerField(max_length=1)




class Medicos(models.Model):
    _idMedico=models.AutoField(primary_key=True)
    Nombre_Medico=models.CharField(max_length=50)
    Apellido_Medico=models.CharField(max_length=50)
    Correo=models.EmailField (max_length = 50)
    Telefono=models.IntegerField(max_length=10)


    class Meta:
        verbose_name='medico'
        verbose_name_plural='medicos'

    def _str_(self):
        return self.Nombre_Medico


class Roles(models.Model): 

    _idRoles= models.AutoField(primary_key=True)
    Tipo=models.CharField(max_length=20)
    Rol=models.CharField(max_length=20)


class Detalle_Historial(models.Model):

    _idDetalle_Historial=models.AutoField(primary_key=True)
    _idConsulta=models.IntegerField(max_length=10)


class Solicitud_Cita(models.Model):

    _idSolicitud=models.AutoField(primary_key=True)
    _idPacientes=models.CharField(max_length=50)
    Estado=models.CharField(max_length=50)
    Fecha_Solicitud=models.EmailField (max_length = 50)
    Hora_Solicitud=models.IntegerField(max_length=10)
    _idMedico=models.IntegerField(max_length=10)
    Tipo_Cosulta=models.CharField(max_length=50)


class Grupos_Familiares(models.Model):

    _idGrupoFamiliar=models.AutoField(primary_key=True)
    _idFamilia=models.IntegerField(max_length=10)
    _idPaciente=models.IntegerField(max_length=10)


class Familia ():

    _idFamilia=models.AutoField(primary_key=True)
    Nombre_familia=models.CharField(max_length=50)
    _idMedico=models.IntegerField(max_length=10)