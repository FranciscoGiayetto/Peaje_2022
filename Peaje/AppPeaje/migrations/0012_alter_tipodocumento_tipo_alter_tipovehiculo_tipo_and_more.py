# Generated by Django 4.1.2 on 2022-11-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppPeaje", "0011_rename_fechaplanificada_turnos_fecha_creacion_and_more")
    ]

    operations = [
        migrations.AlterField(
            model_name="tipodocumento",
            name="tipo",
            field=models.CharField(
                choices=[
                    ("Documento de identidad", "DNI"),
                    ("Pasaporte nacional", "Pasaporte"),
                    ("Internacional", "CIF"),
                ],
                default="DNI",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="tipovehiculo",
            name="tipo",
            field=models.CharField(
                choices=[
                    ("3/4 ejes", "Auto con carro"),
                    ("5/6 ejes", "Camion 5 ejes"),
                    ("3 ejes", "Camion"),
                    ("mas 6 ejes", "Camion mas 6 ejes"),
                    ("1 eje", "Motocicleta"),
                    ("2 ejes", "Auto"),
                ],
                default="",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="turnos",
            name="sentidoCirculacion",
            field=models.CharField(
                choices=[
                    ("S-N", "sur-norte"),
                    ("N-S", "norte-sur"),
                    ("O-E)", "oeste-este"),
                    ("E-O", "este-oeste"),
                ],
                default="este-oeste",
                max_length=10,
            ),
        ),
    ]