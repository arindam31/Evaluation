# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-31 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluator', '0006_exam_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='name',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='question',
        ),
        migrations.AddField(
            model_name='exam',
            name='times_taken',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='exam',
            name='total_questions',
            field=models.IntegerField(default=4),
        ),
    ]