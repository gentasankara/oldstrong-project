# Generated by Django 3.0.7 on 2021-02-19 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motorcycle', '0003_auto_20210219_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motorcycle',
            old_name='make',
            new_name='manufacture',
        ),
    ]
