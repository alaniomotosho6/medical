# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 12:08
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myfield', markdownx.models.MarkdownxField()),
            ],
        ),
    ]
