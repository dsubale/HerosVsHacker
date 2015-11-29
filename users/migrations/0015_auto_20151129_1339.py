# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20151129_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbankapplicationstatus',
            old_name='address_type',
            new_name='status',
        ),
    ]
