# Generated by Django 4.1.7 on 2023-05-03 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_alter_coursecontent_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='outline',
        ),
    ]