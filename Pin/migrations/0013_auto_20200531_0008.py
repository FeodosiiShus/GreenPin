# Generated by Django 3.0.5 on 2020-05-30 21:08

from django.db import migrations, models
import storages.backends.dropbox


class Migration(migrations.Migration):

    dependencies = [
        ('Pin', '0012_auto_20200515_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=storages.backends.dropbox.DropBoxStorage(), upload_to='category/'),
        ),
    ]
