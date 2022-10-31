# Generated by Django 4.1.2 on 2022-10-30 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("AppPeaje", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="tipodocumento",
            name="tipo",
            field=models.CharField(
                choices=[
                    ("Pasaporte nacional", "DNI"),
                    ("Internacional", "CIF"),
                    ("Documento de identidad", "DNI"),
                ],
                default="DNI",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="turnos",
            name="sentidoCirculacion",
            field=models.CharField(
                choices=[
                    ("E-O", "este-oeste"),
                    ("S-N", "sur-norte"),
                    ("O-E)", "oeste-este"),
                    ("N-S", "norte-sur"),
                ],
                default="este-oeste",
                max_length=10,
            ),
        ),
    ]