# Generated by Django 5.0.3 on 2024-06-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd_mascota', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.CharField(blank=True, max_length=45, null=True)),
                ('tipo_consulta', models.IntegerField(choices=[(0, 'consulta'), (1, 'reclamo'), (2, 'sugerencia'), (3, 'felicitaciones')])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
    ]
