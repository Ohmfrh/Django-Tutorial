# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 03:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160411_0324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TestLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tt', models.CharField(max_length=200)),
                ('test1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Test1')),
            ],
        ),
    ]
