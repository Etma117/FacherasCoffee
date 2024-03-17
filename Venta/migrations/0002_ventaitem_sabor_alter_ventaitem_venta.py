# Generated by Django 4.2.7 on 2024-03-15 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Venta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventaitem',
            name='sabor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ventaitem',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle', to='Venta.venta'),
        ),
    ]
