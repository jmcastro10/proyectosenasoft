# Generated by Django 3.1.2 on 2020-10-14 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Historial',
            fields=[
                ('_idDetalle_Historial', models.AutoField(primary_key=True, serialize=False)),
                ('_idConsulta', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Grupos_Familiares',
            fields=[
                ('_idGrupoFamiliar', models.AutoField(primary_key=True, serialize=False)),
                ('_idFamilia', models.IntegerField(max_length=10)),
                ('_idPaciente', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('_idHistorial', models.AutoField(primary_key=True, serialize=False)),
                ('Observacion', models.CharField(max_length=50)),
                ('Aprobacion', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('_idMedico', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_Medico', models.CharField(max_length=50)),
                ('Apellido_Medico', models.CharField(max_length=50)),
                ('Correo', models.EmailField(max_length=50)),
                ('Telefono', models.IntegerField(max_length=10)),
            ],
            options={
                'verbose_name': 'medico',
                'verbose_name_plural': 'medicos',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('_idRoles', models.AutoField(primary_key=True, serialize=False)),
                ('Tipo', models.CharField(max_length=20)),
                ('Rol', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud_Cita',
            fields=[
                ('_idSolicitud', models.AutoField(primary_key=True, serialize=False)),
                ('_idPacientes', models.CharField(max_length=50)),
                ('Estado', models.CharField(max_length=50)),
                ('Fecha_Solicitud', models.EmailField(max_length=50)),
                ('Hora_Solicitud', models.IntegerField(max_length=10)),
                ('_idMedico', models.IntegerField(max_length=10)),
                ('Tipo_Cosulta', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='test',
        ),
        migrations.AlterModelOptions(
            name='pacientes',
            options={'verbose_name': 'paciente', 'verbose_name_plural': 'pacientes'},
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='Dni',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='Telefono',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='correo',
            field=models.EmailField(max_length=50),
        ),
    ]
