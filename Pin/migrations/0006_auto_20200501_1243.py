# Generated by Django 3.0.5 on 2020-05-01 09:43

from django.db import migrations, models
import storages.backends.dropbox


class Migration(migrations.Migration):

    dependencies = [
        ('Pin', '0005_auto_20200422_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='img',
            field=models.ImageField(blank=True, null=True, storage=storages.backends.dropbox.DropBoxStorage(), upload_to=''),
        ),
    ]
