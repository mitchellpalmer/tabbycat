from db_file_storage.storage import DatabaseFileStorage
from django.db import models
from django_summernote.models import AbstractAttachment


class UploadedImage(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)


class BlobAttachment(AbstractAttachment):
    file = models.FileField(
        upload_to='images.UploadedImage/bytes/filename/mimetype',
        storage=DatabaseFileStorage(),
    )
