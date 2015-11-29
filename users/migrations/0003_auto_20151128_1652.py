# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151128_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ifsc', models.CharField(max_length=11, null=True, blank=True)),
                ('branch', models.CharField(max_length=255, null=True, blank=True)),
                ('user_profile', models.ForeignKey(related_name='banks', to='users.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfileAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_type', models.CharField(default=b'permanent', max_length=10, choices=[(b'local', b'Local'), (b'permanent', b'Permanent')])),
                ('co_name', models.CharField(max_length=255, null=True, blank=True)),
                ('house', models.TextField(default=None, null=True, blank=True)),
                ('street_name', models.TextField(default=None, null=True, blank=True)),
                ('landmark', models.TextField(default=None, null=True, blank=True)),
                ('locality', models.TextField(default=None, null=True, blank=True)),
                ('city', models.CharField(max_length=255, null=True, blank=True)),
                ('sub_district_name', models.CharField(max_length=255, null=True, blank=True)),
                ('district_name', models.CharField(max_length=255, null=True, blank=True)),
                ('state', models.CharField(max_length=255, null=True, blank=True)),
                ('pincode', models.CharField(max_length=6, null=True, blank=True)),
                ('post_office_name', models.CharField(max_length=255, null=True, blank=True)),
                ('local_language', models.CharField(max_length=255, null=True, blank=True)),
                ('user_profile', models.ForeignKey(related_name='address', to='users.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='co_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='district_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='house',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='l_city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='l_co_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='l_district_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='l_house',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='l_landmark',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='l_locality',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='l_pincode',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='l_post_office_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='l_state',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='l_street_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='l_sub_district_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='landmark',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='local_language',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='post_office_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='state',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='street_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='sub_district_name',
        ),
    ]
