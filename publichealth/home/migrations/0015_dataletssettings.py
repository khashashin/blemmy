# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-21 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20170421_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataletsSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_question', models.TextField(blank=True, help_text='Send us a question')),
                ('feedback_status', models.IntegerField(blank=True, choices=[(1, ':-('), (2, ':-|'), (3, ':-)'), (4, ':-D')], help_text='How are you enjoying Wagtail?', null=True)),
                ('feedback_comment', models.TextField(blank=True, help_text='Any general feedback')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Datalets',
            },
        ),
    ]