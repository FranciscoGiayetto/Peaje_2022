# Generated by Django 4.1.2 on 2022-11-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppPeaje", "0014_alter_tipodocumento_tipo_alter_tipovehiculo_tipo_and_more")
    ]

    operations = [
        migrations.AlterField(
            model_name="tipodocumento",
            name="tipo",
            field=models.CharField(
                choices=[
                    ("Documento de identidad", "DNI"),
                    ("Internacional", "CIF"),
                    ("Pasaporte nacional", "Pasaporte"),
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
                    ("1 eje", "Motocicleta"),
                    ("2 ejes", "Auto"),
                    ("mas 6 ejes", "Camion mas 6 ejes"),
                    ("3/4 ejes", "Auto con carro"),
                    ("5/6 ejes", "Camion 5 ejes"),
                    ("3 ejes", "Camion"),
                ],
                default="",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="turnos",
            name="HoraPlanificadacomienzo",
            field=models.CharField(
                choices=[
                    ("madrugada", "00:00 - 08:00 "),
                    ("dia", "08:00 - 16:00"),
                    ("noche", "16:00 - 00:00"),
                ],
                default="00:00 - 08:00",
                max_length=14,
            ),
        ),
        migrations.AlterField(
            model_name="turnos",
            name="sentidoCirculacion",
            field=models.CharField(
                choices=[
                    ("N-S", "norte-sur"),
                    ("O-E)", "oeste-este"),
                    ("E-O", "este-oeste"),
                    ("S-N", "sur-norte"),
                ],
                default="este-oeste",
                max_length=10,
            ),
        ),
    ]