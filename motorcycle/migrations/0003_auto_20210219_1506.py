# Generated by Django 3.0.7 on 2021-02-19 07:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motorcycle', '0002_auto_20210219_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]