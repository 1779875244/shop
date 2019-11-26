# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-20 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='分类名称')),
                ('slug', models.CharField(max_length=200, unique=True, verbose_name='slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='产品名称')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='产品图片')),
                ('description', models.TextField(blank=True, verbose_name='产品描述')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='产品价格')),
                ('stock', models.IntegerField(verbose_name='产品库存')),
                ('active', models.BooleanField(default=True, verbose_name='是否激活')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.Category', verbose_name='分类')),
            ],
        ),
    ]
