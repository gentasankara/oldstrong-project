# Generated by Django 3.0.7 on 2021-12-17 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_remove_payments_payment_proof'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='payment_proof',
            field=models.FileField(blank=True, upload_to='media/% Y/% m/% d/'),
        ),
    ]
