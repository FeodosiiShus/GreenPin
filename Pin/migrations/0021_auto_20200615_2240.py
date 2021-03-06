# Generated by Django 3.0.5 on 2020-06-15 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pin', '0020_auto_20200612_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='lat',
            field=models.DecimalField(decimal_places=12, max_digits=14, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='pin',
            name='lng',
            field=models.DecimalField(decimal_places=12, max_digits=14, null=True, verbose_name='Долгота'),
        ),
    ]
