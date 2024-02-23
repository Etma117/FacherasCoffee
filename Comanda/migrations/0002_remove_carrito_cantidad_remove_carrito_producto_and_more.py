# Generated by Django 4.2.7 on 2024-02-22 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0005_alter_producto_sabores_raw'),
        ('Comanda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='carrito',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='carrito',
            name='usuario',
        ),
        migrations.CreateModel(
            name='CarritoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Comanda.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.producto')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(through='Comanda.CarritoItem', to='Menu.producto'),
        ),
    ]