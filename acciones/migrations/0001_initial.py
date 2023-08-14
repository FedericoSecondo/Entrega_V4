# Generated by Django 4.2.3 on 2023-08-08 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simbolo', models.CharField(max_length=10)),
                ('descripcion', models.TextField(default='Descripción', max_length=255)),
                ('fecha_fundacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CompraAccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simbolo', models.CharField(max_length=10)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.PositiveIntegerField(default=1)),
                ('fecha_compra', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ResultadoEconomico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado_ultimo_anio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('proyeccion_proximo_anio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('accion_comprada', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='acciones.compraaccion')),
            ],
        ),
        migrations.CreateModel(
            name='CEOEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_director', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('sitio_web', models.URLField()),
                ('accion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='acciones.accion')),
            ],
        ),
    ]
