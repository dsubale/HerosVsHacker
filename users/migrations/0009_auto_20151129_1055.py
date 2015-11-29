# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20151129_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ifsc', models.CharField(db_index=True, max_length=11, unique=True, null=True, blank=True)),
                ('branch', models.CharField(db_index=True, max_length=255, null=True, blank=True)),
                ('bank_name', models.CharField(db_index=True, max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserBank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bank', models.ForeignKey(related_name='banks', default=None, to='users.Bank')),
                ('user_profile', models.ForeignKey(related_name='banks', to='users.UserProfile')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='bank',
            unique_together=set([('ifsc', 'branch', 'bank_name')]),
        ),
    ]
