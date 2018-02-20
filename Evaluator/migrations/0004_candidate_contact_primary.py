# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-14 18:24
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluator', '0003_auto_20180113_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='contact_primary',
            field=models.IntegerField(null=True, validators=[django.core.validators.RegexValidator(regex='^\\d{10}$')]),
        ),
    ]