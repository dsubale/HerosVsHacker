# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20151128_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(default=b'applicant', max_length=10, choices=[(b'applicant', b'Applicant'), (b'approver', b'Approver')]),
            preserve_default=True,
        ),
    ]
