# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_userprofile_pan_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='permanent',
            field=models.TextField(default=None, null=True, blank=True),
        ),
    ]
