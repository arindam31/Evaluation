# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-05 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluator', '0036_remove_aspect_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingaspect',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
