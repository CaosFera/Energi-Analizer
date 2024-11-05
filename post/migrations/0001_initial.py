# Generated by Django 5.1.1 on 2024-11-01 17:43

import django.contrib.gis.db.models.fields
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lifespan', models.PositiveIntegerField(default=0, verbose_name='Vida Útil (em horas)')),
                ('power', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Potência (W)')),
                ('voltage', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Voltagem (V)')),
                ('current', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Corrente (A)')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Latitude')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Longitude')),
                ('street', models.CharField(default='', max_length=100, verbose_name='Rua')),
                ('district', models.CharField(default='', max_length=100, verbose_name='Bairro')),
                ('city', models.CharField(default='', max_length=100, verbose_name='Cidade')),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data de Manutenção')),
                ('description', models.TextField(blank=True, default='', verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('installation_date', models.DateField(verbose_name='Data de Instalação')),
                ('type_lamp', models.CharField(max_length=50, verbose_name='Tipo de Lâmpada')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo ?')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installation_date', models.DateField(verbose_name='Data de Instalação')),
                ('hub_location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hub_locations', to='post.location')),
            ],
        ),
    ]
