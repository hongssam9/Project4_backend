# Generated by Django 4.0.1 on 2022-01-21 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_rename_photo_comment_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='image',
            new_name='photo',
        ),
    ]
