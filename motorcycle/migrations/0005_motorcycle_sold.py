# Generated by Django 3.0.7 on 2021-12-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorcycle', '0004_auto_20210219_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorcycle',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]