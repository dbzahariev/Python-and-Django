# Generated by Django 2.2.1 on 2019-05-25 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bears', '0003_auto_20190524_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bear',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='bear',
            name='owner',
        ),
    ]
