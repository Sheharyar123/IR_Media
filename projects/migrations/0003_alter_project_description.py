# Generated by Django 4.1.7 on 2023-03-01 16:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_category_options_alter_project_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]