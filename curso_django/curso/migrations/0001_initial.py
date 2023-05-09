# Generated by Django 4.2 on 2023-05-07 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alumno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=20)),
                ("apellido", models.CharField(max_length=20)),
                ("telefono", models.CharField(max_length=20)),
                ("fecha_nacimiento", models.DateField()),
                ("codigo", models.IntegerField()),
            ],
        ),
    ]
