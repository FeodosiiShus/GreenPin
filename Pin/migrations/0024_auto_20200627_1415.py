# Generated by Django 3.0.5 on 2020-06-27 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pin', '0023_statuspin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statuspin',
            options={'verbose_name': 'Статус нарушения', 'verbose_name_plural': 'Cтатусы нарушений'},
        ),
    ]
