# Generated by Django 3.0.5 on 2020-05-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pin', '0008_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
