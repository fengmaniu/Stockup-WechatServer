# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_remove_user_basic_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='news_collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newscollection_url', models.CharField(max_length=200)),
                ('newscollection_pic', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.User_basic')),
            ],
        ),
        migrations.CreateModel(
            name='news_personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newspersonal_url', models.CharField(max_length=200)),
                ('newspersonal_pic', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.User_basic')),
            ],
        ),
        migrations.CreateModel(
            name='stock_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=200)),
                ('stock_amount', models.CharField(max_length=200)),
                ('stockvalue_daily', models.CharField(max_length=200)),
                ('date_whenbuy', models.DateTimeField(verbose_name='date buy stock')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.User_basic')),
            ],
        ),
        migrations.CreateModel(
            name='User_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_portrait', models.CharField(max_length=200)),
                ('user_gender', models.CharField(max_length=200)),
                ('user_address', models.CharField(max_length=200)),
                ('user_wechatnum', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.User_basic')),
            ],
        ),
    ]