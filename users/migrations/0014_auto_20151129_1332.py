# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20151129_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBankApplicationStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ifsc', models.CharField(db_index=True, max_length=11, null=True, blank=True)),
                ('address_type', models.CharField(default=b'permanent', max_length=10, choices=[(b'applied', b'Applied'), (b'rejected', b'Rejected'), (b'approved', b'Approved')])),
                ('applied_on', models.DateTimeField(db_index=True, null=True, blank=True)),
                ('user_profile', models.ForeignKey(related_name='bankapplications', to='users.UserProfile')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='userbankapplicationstatus',
            unique_together=set([('user_profile', 'ifsc')]),
        ),
    ]
