# Generated by Django 5.0 on 2023-12-18 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
