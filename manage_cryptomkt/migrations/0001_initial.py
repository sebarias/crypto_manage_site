# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 16:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12)),
                ('tipo', models.CharField(max_length=10, null=True)),
                ('moneda', models.CharField(max_length=5, null=True)),
                ('mercado', models.CharField(max_length=200, null=True)),
                ('coin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manage_cryptomkt.Coin')),
            ],
        ),
    ]