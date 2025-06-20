# Generated by Django 5.1.7 on 2025-06-02 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dataset",
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
                ("titulo", models.CharField(max_length=200, verbose_name="Título")),
                ("descripcion", models.TextField(verbose_name="Descripción")),
                (
                    "imagen",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="certificados",
                        verbose_name="Certificado",
                    ),
                ),
                (
                    "archivo_html",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="certificados",
                        verbose_name="Certificado",
                    ),
                ),
                (
                    "creado",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de subida"
                    ),
                ),
            ],
            options={
                "verbose_name": "dataset",
                "verbose_name_plural": "datasets",
                "ordering": ["-creado"],
            },
        ),
    ]
