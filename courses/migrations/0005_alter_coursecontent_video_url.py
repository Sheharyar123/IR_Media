# Generated by Django 4.1.7 on 2023-05-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_coursecontent_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecontent',
            name='video_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
