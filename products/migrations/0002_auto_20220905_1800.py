# Generated by Django 3.2 on 2022-09-05 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='location',
        ),
        migrations.RemoveField(
            model_name='product',
            name='varietal',
        ),
    ]
