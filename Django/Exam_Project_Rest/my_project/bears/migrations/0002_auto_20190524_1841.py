# Generated by Django 2.2.1 on 2019-05-24 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bears', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bear',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bears', to='bears.ProfileUser'),
        ),
    ]
