# Generated by Django 3.2.9 on 2021-11-29 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBebidas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cerveza',
            name='capacidad',
            field=models.IntegerField(),
        ),
    ]