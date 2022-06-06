# Generated by Django 4.0.4 on 2022-05-25 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import news.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='date',
            new_name='timestamp',
        ),
        migrations.AddField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=news.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='articles',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
