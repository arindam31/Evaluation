# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-28 12:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluator', '0026_auto_20180928_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='rating_sheet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Evaluator.RatingSheet'),
        ),
    ]
