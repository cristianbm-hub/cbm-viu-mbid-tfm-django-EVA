# Generated by Django 5.0 on 2023-12-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="usuario",
            name="codigo_usuario",
            field=models.CharField(default="", max_length=20, unique=True),
        ),
    ]
