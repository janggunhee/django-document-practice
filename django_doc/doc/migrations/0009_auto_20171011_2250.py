# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0008_auto_20171011_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('debut_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Idol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_date', models.DateField()),
                ('is_active', models.BooleanField()),
                ('Group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.Group')),
                ('idol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.Idol')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='doc.Membership', to='doc.Idol'),
        ),
    ]
