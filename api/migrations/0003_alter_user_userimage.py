# Generated by Django 4.0.5 on 2022-07-17 04:02

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userimage',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.image_directory_path),
        ),
    ]