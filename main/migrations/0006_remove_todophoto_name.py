# Generated by Django 4.0.1 on 2023-06-24 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_todophoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todophoto',
            name='name',
        ),
    ]