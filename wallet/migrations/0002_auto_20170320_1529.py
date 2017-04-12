# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='address',
            field=models.CharField(default='URL or Platform', max_length=75),
        ),
        migrations.AddField(
            model_name='card',
            name='notes',
            field=models.TextField(default='put extra notes down here', max_length=225),
        ),
        migrations.AddField(
            model_name='card',
            name='title',
            field=models.CharField(default='Card Title', max_length=45),
        ),
        migrations.AlterField(
            model_name='card',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='card',
            name='password',
            field=models.CharField(default='password', max_length=125),
        ),
        migrations.AlterField(
            model_name='card',
            name='username',
            field=models.CharField(default='UserName', max_length=35),
        ),
    ]