# Generated by Django 4.0.1 on 2022-01-14 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_comment_date_created_photo_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date_created',
        ),
    ]
