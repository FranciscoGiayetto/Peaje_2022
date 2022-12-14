# Generated by Django 4.1.2 on 2022-12-02 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppPeaje", "0015_alter_tipodocumento_tipo_alter_tipovehiculo_tipo_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tipodocumento",
            name="tipo",
            field=models.CharField(
                choices=[("Pasaporte", "Pasaporte"), ("DNI", "DNI"), ("CIF", "CIF")],
                default="DNI",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="tipovehiculo",
            name="tipo",
            field=models.CharField(
                choices=[
                    ("5/6 ejes", "5/6 ejes"),
                    ("Automoviles", "Automoviles"),
                    ("3/4 ejes < 2.10m", "3/4 ejes < 2.10m"),
                    ("3/4 ejes > 2.10m", "3/4 ejes > 2.10m"),
                    ("Motocicletas", "Motocicletas"),
                    ("2 ejes", "2 ejes"),
                    ("> 6 ejes", "> 6 ejes"),
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
                    ("sur-norte", "sur-norte"),
                    ("este-oeste", "este-oeste"),
                    ("norte-sur", "norte-sur"),
                    ("oeste-este", "oeste-este"),
                ],
                default="este-oeste",
                max_length=10,
            ),
        ),
    ]
