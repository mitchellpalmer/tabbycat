# Generated by Django 3.1.1 on 2020-09-20 10:18

import db_file_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20200920_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blobattachment',
            name='file',
            field=models.FileField(storage=db_file_storage.storage.DatabaseFileStorage(), upload_to='images.UploadedImage/bytes/filename/mimetype'),
        ),
    ]
