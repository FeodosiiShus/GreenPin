# Generated by Django 3.0.5 on 2020-04-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pin', '0003_auto_20200422_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
