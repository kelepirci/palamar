# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0002_auto_20161202_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('type', models.CharField(choices=[('1', 'Public Cloud Provider'), ('2', 'Private Cloud Provider'), ('3', 'Container Provider'), ('4', 'VPS Provider')], max_length=1)),
                ('logo', models.FileField(upload_to='static/provider-logo/')),
            ],
        ),
    ]