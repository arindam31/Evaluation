# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-11 09:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Evaluator', '0049_auto_20190123_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='supporting_interviewer',
            field=models.ManyToManyField(blank=True, null=True, related_name='supporters', to=settings.AUTH_USER_MODEL),
        ),
    ]
