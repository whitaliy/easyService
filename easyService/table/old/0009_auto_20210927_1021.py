# Generated by Django 3.2.7 on 2021-09-27 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0008_auto_20210927_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='object',
            name='level',
        ),
        migrations.RemoveField(
            model_name='object',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='object',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='object',
            name='tree_id',
        ),
    ]
