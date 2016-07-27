# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 06:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('family', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('typecontact', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='contact_phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('personcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.contact')),
            ],
        ),
    ]
