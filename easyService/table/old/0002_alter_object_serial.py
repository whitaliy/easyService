# Generated by Django 3.2.7 on 2021-09-08 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='serial',
            field=models.BigIntegerField(error_messages={'unique': 'Поле должно быть уникальным'}, unique=True, verbose_name='инв. номер'),
        ),
    ]