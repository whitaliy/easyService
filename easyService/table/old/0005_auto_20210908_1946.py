# Generated by Django 3.2.7 on 2021-09-08 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0004_auto_20210908_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='buildings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.buildings', verbose_name='Корпус'),
        ),
        migrations.AlterField(
            model_name='object',
            name='cabinet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='objects', to='table.сabinet', verbose_name='Помещение'),
        ),
        migrations.AlterField(
            model_name='object',
            name='dir',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.dir', verbose_name='Категория'),
        ),
    ]
