# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_cryptomkt', '0002_precio_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precio',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
