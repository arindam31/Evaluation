# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-22 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluator', '0048_auto_20181227_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='skill',
            field=models.ManyToManyField(blank=True, to='Evaluator.Skill'),
        ),
    ]
