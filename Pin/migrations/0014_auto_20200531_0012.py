# Generated by Django 3.0.5 on 2020-05-30 21:12

from django.db import migrations, models
import storages.backends.dropbox


class Migration(migrations.Migration):

    dependencies = [
        ('Pin', '0013_auto_20200531_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=storages.backends.dropbox.DropBoxStorage(), upload_to='category'),
        ),
    ]