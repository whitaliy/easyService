# Generated by Django 3.2.7 on 2021-09-27 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0007_auto_20210913_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='level',
            field=models.PositiveIntegerField(default='timezone.now', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='object',
            name='lft',
            field=models.PositiveIntegerField(default='timezone.now', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='object',
            name='rght',
            field=models.PositiveIntegerField(default='timezone.now', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='object',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default='timezone.now', editable=False),
            preserve_default=False,
        ),
    ]
