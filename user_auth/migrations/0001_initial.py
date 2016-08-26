# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('first_name', models.CharField(max_length=80, null=True, blank=True)),
                ('middle_name', models.CharField(max_length=80, null=True, blank=True)),
                ('last_name', models.CharField(max_length=80, null=True, blank=True)),
                ('full_name', models.CharField(max_length=80, null=True, blank=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=50, null=True, blank=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, unique=True, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format:'         ' '+999999999'. Up to 15 digits allowed.")])),
                ('country_code', models.CharField(max_length=6, null=True, blank=True)),
                ('role', models.CharField(default=b'Normal User', max_length=50, null=True, choices=[(b'Agent', b'AGENT'), (b'Normal User', b'NORMAL USER'), (b'Super User', b'SUPER USER')])),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
