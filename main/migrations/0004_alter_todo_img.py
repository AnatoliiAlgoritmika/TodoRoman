# Generated by Django 4.0.1 on 2023-06-20 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_todo_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='img',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images'),
        ),
    ]