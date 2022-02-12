# Generated by Django 4.0.2 on 2022-02-12 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.fields.related


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=5)),
                ('size', models.BigIntegerField()),
                ('file_url', models.CharField(max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.fields.related.ForeignKey, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]