# Generated by Django 3.0.7 on 2021-12-17 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payments_payment_proof'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='payment_proof',
        ),
    ]
