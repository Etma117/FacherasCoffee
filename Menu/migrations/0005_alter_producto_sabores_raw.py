# Generated by Django 3.2.20 on 2024-02-18 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0004_auto_20240212_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='sabores_raw',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]