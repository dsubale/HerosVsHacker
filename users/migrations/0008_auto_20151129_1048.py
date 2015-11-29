# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20151129_1039'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bank',
        ),
        migrations.RemoveField(
            model_name='userbank',
            name='bank',
        ),
        migrations.RemoveField(
            model_name='userbank',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='UserBank',
        ),
    ]
