# Generated by Django 3.0.5 on 2020-05-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pin', '0009_pin_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pin',
            name='geo',
        ),
        migrations.AddField(
            model_name='pin',
            name='lat',
            field=models.TextField(default='1', verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='pin',
            name='lng',
            field=models.TextField(default='1', verbose_name='Долгота'),
        ),
    ]