# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    pass

    dependencies = [
        ('users', '0006_auto_20151128_2044'),
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
        migrations.RemoveField(
            model_name='userbank',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='userbank',
            name='ifsc',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=None, unique=True, max_length=254, db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name='bank',
            unique_together=set([('ifsc', 'branch', 'bank_name')]),
        ),
        migrations.AddField(
            model_name='userbank',
            name='bank',
            field=models.ForeignKey(related_name='banks', default=None, to='users.Bank'),
        ),
    ]
