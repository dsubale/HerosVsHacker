# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20151129_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pan_card',
            field=models.CharField(default=None, max_length=10, null=True, db_index=True, blank=True),
        ),
    ]
