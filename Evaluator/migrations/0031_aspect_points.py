# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-29 19:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluator', '0030_rating_interview'),
    ]

    operations = [
        migrations.AddField(
            model_name='aspect',
            name='points',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]