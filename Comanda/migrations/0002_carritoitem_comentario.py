# Generated by Django 3.2.20 on 2024-03-17 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comanda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carritoitem',
            name='comentario',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
