from django.db import models
from django.contrib.auth.models import User
from django_minio_backend import MinioBackend, iso_date_prefix

class UploadedFile(models.Model):
    user = models.ForeignKey(User , on_delete=models.ForeignKey)
    type = models.CharField(max_length=5)
    size = models.BigIntegerField()
    file = models.FileField(storage=MinioBackend(bucket_name='test'), upload_to=iso_date_prefix)

